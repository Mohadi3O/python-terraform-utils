# std

# internal
import terraform_model.utils.utils
from .code import Code
from . import utils
from .utils import create_init_method, add_attributes
from terraform_model.blocks.blocks.resource import Resource


# constants
RESOURCE_PATH = f'{Resource.__module__}.{Resource.__qualname__}'


def compile_resource(name: str, resource_schema: dict) -> str:
    code = Code()
    utils.append_imports(code)
    _compile_block(name, resource_schema, code)
    code.append('')
    return code.compile()


def _compile_block(name: str, schema: dict, code: Code):
    class_name = terraform_model.utils.utils.get_class_name(name)
    class_ = code.class_(class_name, RESOURCE_PATH)
    block_types = schema.get('block_types', {})
    for name, block_type in block_types.items():
        _compile_block(name, block_type, class_)
    block_schema = schema.get('block', {})
    create_init_method(class_, block_schema, name)
    add_attributes(class_, block_schema)
