def terraform():
    from os import system
    from sys import argv
    from .is_installed import is_terraform_installed
    if not is_terraform_installed():
        from .install import install_terraform
        install_terraform()
    from .constants import TERRAFORM_PATH
    system(' '.join([TERRAFORM_PATH] + argv[1:]))
