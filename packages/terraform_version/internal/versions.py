from contextlib import contextmanager
from distutils.version import StrictVersion
import http.client
import os
import re


PYPROJECT_TOML_VERSION_PATTERN = r'^version = "\d+\.\d+\.\d+"$'
TERRAFORM_VERSION_PATTERN = r'terraform_(\d+\.\d+\.\d+)'


@contextmanager
def https_connection(url: str):
    conn = http.client.HTTPSConnection(url)
    try:
        yield conn
    finally:
        conn.close()


def get_terraform_versions():
    with https_connection('releases.hashicorp.com') as conn:
        conn.request('GET', '/terraform/')
        html = conn.getresponse().read().decode('utf-8')
        versions = re.findall(TERRAFORM_VERSION_PATTERN, html)
        versions.sort(key=StrictVersion)
        return versions


def is_in_pypi(version):
    with https_connection('pypi.org') as conn:
        conn.request('GET', f'/pypi/terraform-version/{version}/json')
        response = conn.getresponse()
        return response.status == 200


def update_version(version: str):
    with open('terraform_version/version.py', 'w') as fh:
        fh.write(f'__version__ = \'{version}\'\n')
    with open('./pyproject.toml', 'r') as fh:
        content = fh.read()
    content = '\n'.join(
        [re.sub(PYPROJECT_TOML_VERSION_PATTERN, f'version = "{version}"', line) for line in content.split('\n')]
    )
    with open('./pyproject.toml', 'w') as fh:
        fh.write(content)


def build_and_publish():
    os.system('poetry build')
    os.system('poetry publish')


if __name__ == '__main__':
    assert(os.path.basename(os.getcwd()) == 'terraform_version')
    assert(os.path.isdir('./terraform_version'))
    versions = get_terraform_versions()
    versions = versions[0:6]  # TODO: delete this line
    for version in versions:
        if version not in ['0.1.0', '0.1.1'] and not is_in_pypi(version):
            print(f'Adding {version}')
            update_version(version)
            build_and_publish()
