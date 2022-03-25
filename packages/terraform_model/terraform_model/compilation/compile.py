# std
from functools import cache
import importlib.util


@cache
def import_module_from_filepath(filepath: str):
    module_name = '__model__'
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
