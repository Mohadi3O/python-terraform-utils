# std
from contextlib import contextmanager
import http.client
import os
import pathlib
import platform
import shutil
import tempfile
import zipfile

# external
from terraform_version import __version__

# internal
from .constants import TERRAFORM_RELEASES_DIR


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


def get_terraform_version_name() -> str:
    arch = get_architecture()
    system = get_system()
    return f'terraform_{__version__}_{system}_{arch}'


def get_terraform_download_zip_filename() -> str:
    return f'{get_terraform_version_name()}.zip'


def get_terraform_download_path() -> str:
    return f'/terraform/{__version__}/{get_terraform_download_zip_filename()}'


def install_terraform():
    print(f'Installing Terraform v{__version__}')
    with tmp_dir():
        with https_connection('releases.hashicorp.com') as conn:
            conn.request('GET', get_terraform_download_path())
            response = conn.getresponse()
            if response.status >= 300:
                raise Exception(f'http status code {response.status}: {response.reason}')
            with open(get_terraform_download_zip_filename(), 'wb') as fh:
                fh.write(response.read())
        with zipfile.ZipFile(get_terraform_download_zip_filename(), 'r') as zf:
            zf.extractall()
        os.chmod('terraform', 0o777)
        folder = os.path.join(TERRAFORM_RELEASES_DIR, get_terraform_version_name())
        pathlib.Path(folder).mkdir(parents=True, exist_ok=True)
        shutil.copy('./terraform', folder)
        os.symlink(folder, os.path.join(TERRAFORM_RELEASES_DIR, __version__))
