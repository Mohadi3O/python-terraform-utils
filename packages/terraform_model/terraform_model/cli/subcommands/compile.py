# std
from functools import cache
import importlib.util
import os

# internal
from terraform_model.utils.logger import log
from terraform_model.model import compile_terraform
from terraform_model.cli.subcommands.terraform import validate


def _validate(args):
    if not os.path.isfile(args.filepath):
        log.error(f'File {args.filepath} does not exist')
        exit(1)


@cache
def import_module(filepath: str):
    module_name = '__model__'
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def compile_terraform_model(args):
    log.info(f'Compiling terraform model from file {args.filepath}')
    _validate(args)
    _ = import_module(args.filepath)
    compile_terraform()
    validate(args)
