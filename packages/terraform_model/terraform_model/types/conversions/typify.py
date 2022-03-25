# std
from typing import Type, Union

# internal
from terraform_model.internal.tftype import tftype, is_type_or_generic
from terraform_model.types.primitives import TfPrimitive, null, true, false, \
    TfNumber, TfNumberLiteral, TfString, TfStringLiteral
from terraform_model.types.collections import TfCollection, TfList, TfListLiteral, \
    TfMap, TfMapLiteral, TfSetLiteral
from terraform_model.types.internal.tftype import TfType
from terraform_model.types.internal.tfunknown import tfunknown
from terraform_model.utils.errors import TerraformConversionError
from terraform_model.utils.types import JsonPrimitive
from terraform_model.internal.deferred import deferred

# types
collection_like = Union[list, dict]
coercable = Union[JsonPrimitive, collection_like, TfType]


def typify_or_get_type(something: any) -> Union[TfType, Type[TfType]]:
    if not is_type_or_generic(something):
        return typify(something)
    else:
        return tftype(something)


def typify(something: any) -> TfType:
    if isinstance(something, TfType):
        return something
    elif isinstance(something, deferred.Block):
        return _typify_block(something)
    try:
        return _typify_primitive(something)
    except TerraformConversionError:
        pass
    try:
        return _typify_collection(something)
    except TerraformConversionError:
        pass
    return tfunknown(something)


def is_primitive(something: any) -> bool:
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
            isinstance(something, TfCollection)
    )


def non_literal(something: TfType) -> TfType:
    return tftype(something)(something)


def to(this, that) -> TfType:
    """Convert this into (non-literal) type of that"""
    return tftype(that).new(this)


def _typify_block(block) -> TfType:
    if isinstance(block, deferred.Variable):
        return _typify_variable(block)
    elif isinstance(block, deferred.Local):
        return _typify_local(block)
    elif isinstance(block, deferred.Output):
        return _typify_output(block)
    return tfunknown(block)


def _typify_variable(var) -> TfType:
    if 'type' in var.data:
        return tftype(var.data['type'])(var)
    if 'default' in var.data:
        return tftype(var.data['default'])(var)
    return tfunknown(var)


def _typify_local(local) -> TfType:
    return tftype(local.value).new(local)


def _typify_output(output) -> TfType:
    return tftype(output.data['value'])(output)


def _typify_primitive(value: Union[JsonPrimitive, TfPrimitive]) -> TfPrimitive:
    if isinstance(value, TfPrimitive):
        return value
    elif value is None:
        return null
    elif value is True:
        return true
    elif value is False:
        return false
    elif isinstance(value, (float, int)):
        return TfNumberLiteral(value)
    elif isinstance(value, str):
        return TfStringLiteral(value)
    else:
        raise TerraformConversionError(f'Cannot coerce {value} to Primitive')


def _typify_collection(collection: Union[collection_like, TfCollection]) -> TfCollection:
    if isinstance(collection, TfCollection):
        return collection
    elif isinstance(collection, list):
        return TfListLiteral(list(map(typify, collection)))
    elif isinstance(collection, dict):
        return TfMapLiteral({key: typify(val) for key, val in collection.items()})
    elif isinstance(collection, set):
        return TfSetLiteral(set(map(typify, collection)))
    else:
        raise TerraformConversionError(f'Cannot coerce {collection} to Collection')


