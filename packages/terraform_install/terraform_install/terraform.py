def terraform():
    from os import system
    from os.path import expanduser, join
    from sys import argv
    from terraform_version import __version__
    terraform_path = join(expanduser('~'), '.terraform-utils/releases', __version__, 'terraform')
    system(' '.join([terraform_path] + argv[1:]))
