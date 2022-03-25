# std
from inspect import Parameter
from typing import Union
import os

# internal
from terraform_model.utils.errors import TerraformTypeError
from terraform_model.internal.tftype import tftype, get_type_like
from terraform_model.internal.deferred import deferred
from terraform_model.gen.code import Class, SELF, Code
from terraform_model.expressions.expressions.getattr import GetAttr

# constants
GET_ATTR = f'{GetAttr.__module__}.{GetAttr.__qualname__}'


def convert_filepath_to_module_path(filepath: str) -> str:
    return os.path.splitext(filepath)[0].replace(os.path.sep, '.')


def append_imports(code: Code):
    code.append(
        'from typing import Union',
        'import terraform_model',
        '',
        '',
    )


def class_path(cls: type) -> str:
    if _is_generic(cls):
        return _generic_class_path(cls)
    return f'{cls.__module__}.{cls.__name__}'


def _is_generic(cls: type) -> bool:
    return hasattr(cls, '__origin__') and hasattr(cls, '__args__')


def _generic_class_path(cls: type) -> str:
    origin = getattr(cls, '__origin__')
    args = getattr(cls, '__args__')
    return f'{class_path(origin)}[{", ".join(map(class_path, args))}]'


def create_init_method(class_: Class, block_schema: dict, sub_type: str):
    parameters = get_parameters(block_schema)
    method = class_.method('__init__', parameters)
    kwargs = 'dict(' + ', '.join((f'{p["name"]}={p["name"]}' for p in parameters if p['name'] != 'local_name')) + ')'
    method.append(f'super().__init__("{sub_type}", local_name, **{kwargs})')


def add_attributes(class_: Class, block_schema: dict):
    for name, schema in block_schema.get('attributes', {}).items():
        return_annotation = tftype(schema.get('type', 'unknown'))
        _add_attribute(class_, name, return_annotation)


def _add_attribute(class_: Class, attribute_name: str, return_annotation: type):
    p = class_.property(attribute_name, annotation=return_annotation)
    p.append(f'return {class_path(return_annotation)}({GET_ATTR}({SELF}, "{attribute_name}"))')
    p.append('')


def get_parameters(block_schema: dict) -> list[dict]:
    parameters = [{
        'name': 'local_name',
        'kind': Parameter.POSITIONAL_ONLY,
        'annotation': get_type_like('string'),
    }]
    for name, attribute in block_schema.get('attributes', {}).items():
        if attribute.get('computed', False):
            continue
        parameter = {
            'name': name,
            'annotation': get_type_like(attribute['type']),
        }
        if attribute.get('optional', False):
            parameter['default'] = None
        parameters.append(parameter)
    return parameters


def is_str_list_type_definition(obj) -> bool:
    return (
            isinstance(obj, str)
            or (isinstance(obj, list) and obj[0] in ('list', 'map', 'set', 'object', 'tuple'))
    )


def get_type_from_str_list_type_definition(obj: Union[str, list[str]]):
    # list indicates a collection or structural type
    if isinstance(obj, list):
        # list indicates a collection or structural type
        collection_or_structural_type = get_type_from_str_list_type_definition(obj[0])
        if issubclass(collection_or_structural_type, deferred.TfCollectionFunction):
            return collection_or_structural_type[get_type_from_str_list_type_definition(obj[1])]
        if issubclass(collection_or_structural_type, deferred.TfStructural):
            raise NotImplementedError
        else:
            raise TerraformTypeError(
                f'{collection_or_structural_type} is not a collection or structure type')
    return {
        # primitives
        'bool': deferred.TfBool,
        'null': deferred.TfNull,
        'number': deferred.TfNumber,
        'string': deferred.TfString,
        # collections
        'list': deferred.TfList,
        'map': deferred.TfMap,
        'set': deferred.TfSet,
        # structurals
        'object': deferred.TfObject,
        'tuple': deferred.TfTuple,
        # unknown
        'unknown': deferred.TfUnknown,
    }.get(obj, deferred.TfUnknown)
