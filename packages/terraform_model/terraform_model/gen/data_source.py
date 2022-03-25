# std

# internal
import terraform_model.utils.utils
from .code import Code
from . import utils
from .utils import create_init_method, add_attributes
from terraform_model.blocks.blocks.data import Data


# constants
DATA_PATH = f'{Data.__module__}.{Data.__qualname__}'


def compile_data_source(name: str, data_source_schema: dict) -> str:
    code = Code()
    utils.append_imports(code)
    block_schema = data_source_schema.get('block', {})
    class_name = _get_class_name(name)
    class_ = code.class_(class_name, DATA_PATH)
    create_init_method(class_, block_schema, name)
    add_attributes(class_, block_schema)
    code.append('')
    return code.compile()


def _get_class_name(name: str) -> str:
    return f'Data{terraform_model.utils.utils.get_class_name(name)}'
