from contextlib import contextmanager
import http.client
import os
import pathlib
import platform
import shutil
import tempfile
import zipfile


TERRAFORM_UTILS_DIR = os.path.join(os.path.expanduser('~'), '.terraform-utils')
TERRAFORM_RELEASES_DIR = os.path.join(TERRAFORM_UTILS_DIR, 'releases')


@contextmanager
def tmp_dir():
    cwd = os.getcwd()
    try:
        with tempfile.TemporaryDirectory() as tmp:
            os.chdir(tmp)
            yield tmp
    finally:
        os.chdir(cwd)


@contextmanager
def https_connection(url: str):
    conn = http.client.HTTPSConnection(url)
    try:
        yield conn
    finally:
        conn.close()


def get_architecture() -> str:
    try:
        return {
            'x86_64': 'amd64',
        }[platform.machine()]
    except KeyError:
        raise Exception(f'Machine "{platform.machine()}" not supported.')


def get_system() -> str:
    return platform.system().lower()


def get_terraform_version_name(version: str) -> str:
    arch = get_architecture()
    system = get_system()
    return f'terraform_{version}_{system}_{arch}'


def get_terraform_download_zip_filename(version: str) -> str:
    return f'{get_terraform_version_name(version)}.zip'


def get_terraform_download_path(version: str) -> str:
    return f'/terraform/{version}/{get_terraform_download_zip_filename(version)}'


def is_release_cached(version: str) -> bool:
    filepath = os.path.join(TERRAFORM_RELEASES_DIR, get_terraform_version_name(version),
                            'terraform')
    return os.path.isfile(filepath)


def download_terraform(version: str):
    with tmp_dir() as tmp:
        with https_connection('releases.hashicorp.com') as conn:
            conn.request('GET', get_terraform_download_path(version))
            response = conn.getresponse()
            if response.status >= 300:
                raise Exception(f'http status code {response.status}: {response.reason}')
            with open(get_terraform_download_zip_filename(version), 'wb') as fh:
                fh.write(response.read())
        with zipfile.ZipFile(get_terraform_download_zip_filename(version), 'r') as zf:
            zf.extractall()
        os.chmod('terraform', 0o777)
        folder = os.path.join(TERRAFORM_RELEASES_DIR, get_terraform_version_name(version))
        pathlib.Path(folder).mkdir(parents=True, exist_ok=True)
        shutil.copy('./terraform', folder)
        os.symlink(folder, os.path.join(TERRAFORM_RELEASES_DIR, version))


def get_terraform_version() -> str:
    import terraform_version
    return terraform_version.__version__


def install_terraform():
    version = get_terraform_version()
    if not is_release_cached(version):
        download_terraform(version)
