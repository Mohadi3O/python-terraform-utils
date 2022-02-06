# std
from functools import cache

# internal
from terraform_model.model import DIST
from terraform_model.utils import log


def terraform(args):
    log.info(f'Running terraform {" ".join(args.args)}')
    tf = default_terraform()
    tf(*args.args)


def validate(args):
    if args.init or args.validate:
        tf = default_terraform()
        if args.init:
            log.info(f'Initializing terraform model')
            tf.init()
        if args.validate:
            log.info(f'Validating terraform model')
            tf.validate()


@cache
def default_terraform():
    from py_terraform import Terraform
    return Terraform(global_call_kwargs={'cwd': DIST})
