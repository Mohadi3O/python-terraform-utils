from typing import Type, Union

from terraform_model.types.atomics import Atomic, null, true, false, \
    Number, NumberLiteral, String, StringLiteral
from terraform_model.types.atomics.bool import Bool
from terraform_model.types.atomics.null import Null
from terraform_model.types.collections import Collection, List, ListLiteral, Map, MapLiteral
from terraform_model.types.terraform_type import TerraformType
from terraform_model.types.unknown import Unknown
from terraform_model.utils.errors import TerraformModelException, TerraformTypeError
from terraform_model.utils.types import JsonAtomic
from terraform_model.utils.deferred import deferred

collection_like = Union[list, dict]
coercable = Union[JsonAtomic, collection_like, TerraformType]


def get_type(name: str) -> Type[TerraformType]:
    return {
        'bool': Bool,
        'null': Null,
        'number': Number,
        'string': String,
        'list': List,
        'map': Map,
    }[name]


def is_atomic(something: any) -> bool:
    return (
            isinstance(something, int) or
            isinstance(something, float) or
            isinstance(something, str) or
            isinstance(something, bool) or
            something is None
    )


def is_collection(something: any) -> bool:
    return (
            isinstance(something, list) or
            isinstance(something, dict) or
            isinstance(something, Collection)
    )


def python_type_to_terraform_type(python_type) -> type(TerraformType):
    if python_type is bool:
        return Bool
    elif python_type is type(None) or python_type is None:
        return Null
    elif python_type is float or python_type is int or python_type is Union[float, int]:
        return Number
    elif python_type is str:
        return String
    elif python_type is list:
        return List
    elif python_type is dict:
        return Map
    else:
        raise TerraformTypeError(f'{python_type} does not have a corresponding TerraformType')


def non_literal_type(something: TerraformType) -> type(TerraformType):
    if isinstance(something, ListLiteral):
        return List
    elif isinstance(something, MapLiteral):
        return Map
    elif isinstance(something, NumberLiteral):
        return Number
    elif isinstance(something, StringLiteral):
        return String
    return something.__class__


def non_literal(something: TerraformType) -> TerraformType:
    return non_literal_type(something)(something)


def to_bool(something) -> Bool:
    return Bool.new(something)


def to_null(_) -> Null:
    return null


def to_number(something) -> Number:
    return Number.new(something)


def to_string(something) -> String:
    return String.new(something)


def to_list(something) -> List:
    return List.new(something)


def to_map(something) -> Map:
    return Map.new(something)


def to(this, that) -> TerraformType:
    """Convert this into (non-literal) type of that"""
    return non_literal_type(that).new(this)


def typify_block(block) -> TerraformType:
    if isinstance(block, deferred.Variable):
        return _typify_variable(block)
    return Unknown(block)


def _typify_variable(var) -> TerraformType:
    if 'type' in var.data:
        return get_type(str(var.data['type']))(var)
    if 'default' in var.data:
        return non_literal_type(var.data['default'])(var)
    return Unknown(var)


def typify_atomic(value: Union[JsonAtomic, Atomic]) -> Atomic:
    if isinstance(value, Atomic):
        return value
    elif value is None:
        return null
    elif value is True:
        return true
    elif value is False:
        return false
    elif isinstance(value, (float, int)):
        return NumberLiteral(value)
    elif isinstance(value, str):
        return StringLiteral(value)
    else:
        raise TerraformModelException(f'Cannot coerce {value} to Atomic')


def typify_collection(collection: Union[collection_like, Collection]) -> Collection:
    if isinstance(collection, Collection):
        return collection
    elif isinstance(collection, list):
        return ListLiteral(list(map(typify, collection)))
    elif isinstance(collection, dict):
        return MapLiteral({key: typify(val) for key, val in collection.items()})
    else:
        raise TerraformModelException(f'Cannot coerce {collection} to Collection')


def typify(something: any) -> TerraformType:
    if isinstance(something, TerraformType):
        return something
    elif isinstance(something, deferred.Block):
        return typify_block(something)
    try:
        return typify_atomic(something)
    except TerraformModelException:
        pass
    try:
        return typify_collection(something)
    except TerraformModelException:
        pass
    return Unknown(something)
