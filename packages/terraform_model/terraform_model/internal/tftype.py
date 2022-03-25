# std
from types import GenericAlias
from typing import cast, Dict, List, Union, Set, Tuple, Type

# internal
from ..utils.errors import TerraformTypeError
from terraform_model.mixins import LiteralMixin
from terraform_model.types.internal.tftype import TfType
from terraform_model.types.internal.tfunknown import TfUnknown
from terraform_model.types.collections import TfCollection
from ..types import TfBool, TfNull, TfNumber, TfString, TfList, TfMap, TfSet, TfTuple
from .deferred import deferred

# types
NullLike = Union[None, TfNull]
BoolLike = Union[bool, TfBool]
NumberLike = Union[int, float, TfNumber]
StringLike = Union[str, TfString]
ListLike = Union[List, TfList]
SetLike = Union[Set, TfSet]
MapLike = Union[Dict, TfMap]
TupleLike = Union[Tuple, TfTuple]
AnyLike = Union[
    BoolLike, NullLike, StringLike, NumberLike, ListLike, MapLike, TupleLike, SetLike, TfType]
TfPrimitiveLike = Union[BoolLike, NullLike, StringLike, NumberLike]
TfJsonLike = Union[TfPrimitiveLike, Dict[str, 'TfJson'], List['TfJson']]
TfJsonObject = Dict[str, TfJsonLike]
TfJsonArray = List[TfJsonLike]

TfTypeInputType = Union[AnyLike, GenericAlias, Type[AnyLike]]

TfTypeOutputTypeShallow = Type[TfType]
TfTypeOutputTypeDeep = GenericAlias
TfTypeOutputType = Union[TfTypeOutputTypeShallow, TfTypeOutputTypeDeep]


def tftype(obj_or_cls: TfTypeInputType, deep: bool = False) -> TfTypeOutputType:
    if is_generic(obj_or_cls):
        return _tftype_from_generic(obj_or_cls, deep)
    elif is_type(obj_or_cls):
        return _tftype_from_type(obj_or_cls)
    elif is_supported_python_obj_or_type(obj_or_cls):
        return _tftype_from_python_obj_or_type(obj_or_cls, deep)
    elif isinstance(obj_or_cls, deferred.Local):
        return _tftype_from_local(obj_or_cls, deep)
    elif isinstance(obj_or_cls, deferred.Variable):
        return _tftype_from_variable(obj_or_cls, deep)
    elif isinstance(obj_or_cls, TfType):
        return _tftype_from_tftype(obj_or_cls, deep)
    else:
        raise TerraformTypeError(f'Unable to get tftype of {repr(obj_or_cls)}')


def is_generic(cls: any) -> bool:
    return (
            not isinstance(cls, deferred.GetAttrMixin)
            and hasattr(cls, '__origin__')
            and hasattr(cls, '__args__')
    )


def _tftype_from_generic(cls: GenericAlias, deep=False) -> TfTypeOutputType:
    if deep:
        return cls
    else:
        return tftype(getattr(cls, '__origin__'))


def is_type(obj) -> bool:
    return obj.__class__ is type


def _tftype_from_type(cls: Union[Type, Type[TfType]]) -> TfTypeOutputType:
    if issubclass(cls, TfType):
        return _tftype_from_type_tf(cls)
    elif _is_supported_python_type(cls):
        return _tftype_from_type_py(cls)
    else:
        raise TerraformTypeError(f'Unable to get tftype of {repr(cls)}')


def _tftype_from_type_tf(cls: Type[TfType]) -> TfTypeOutputType:
    if is_tfliteral(cls):
        return cast(Type[TfType], cls.__base__)
    else:
        return cls


def _tftype_from_type_py(python_type: Type) -> Type[TfType]:
    if python_type is bool:
        return TfBool
    elif python_type is type(None) or python_type is None:
        return TfNull
    elif python_type is float or python_type is int or python_type is Union[float, int]:
        return TfNumber
    elif python_type is str:
        return TfString
    elif python_type is list:
        return TfList
    elif python_type is dict:
        return TfMap
    elif python_type is set:
        return TfSet
    else:
        raise TerraformTypeError(f'{python_type} does not have a corresponding TerraformType')


def _tftype_from_tftype(obj: TfType, deep: bool) -> TfTypeOutputType:
    if isinstance(obj.data, (deferred.Local, deferred.Variable)):
        return tftype(obj.data, deep)
    elif is_tfliteral(obj):
        if deep:
            return tftype(obj.data, deep)
        else:
            return cast(Type[TfType], obj.__class__.__base__)
    elif deep and is_collection(obj):
        tf_origin = _tftype_from_tftype(obj, deep=False)
        tf_arg = get_element_tftype(obj, deep)
        return GenericAlias(tf_origin, (tf_arg,))
    else:
        return obj.__class__


def _tftype_from_local(loc, deep: bool) -> TfTypeOutputType:
    loc = cast(deferred.Local, loc)
    return tftype(loc.value, deep)


def _tftype_from_variable(var, deep: bool) -> TfTypeOutputType:
    var = cast(deferred.Variable, var)
    if var.data.get('type') is not None:
        return tftype(var.data.get('type'), deep)
    elif var.data.get('default') is not None:
        return tftype(var.data.get('default'), deep)
    else:
        return TfUnknown


def is_type_or_generic(something) -> bool:
    return is_type(something) or is_generic(something)


def is_generic_union(cls: any) -> bool:
    return (
            not isinstance(cls, deferred.GetAttrMixin)
            and hasattr(cls, '__origin__')
            and hasattr(cls, '__args__')
            and getattr(cls, '__origin__') is Union
    )


def get_types_from_generic_union(cls: GenericAlias) -> Tuple[Type[TfType]]:
    return getattr(cls, '__args__')


def get_element_type_from_generic(cls: GenericAlias, deep: bool = False) -> Type[TfType]:
    return getattr(cls, '__args__')


def _tftype_from_tfliteral(obj: TfType, deep: bool = False) -> TfTypeOutputType:
    if deep:
        raise NotImplementedError
    else:
        raise NotImplementedError


def is_tfliteral(obj_or_cls) -> bool:
    if is_type(obj_or_cls):
        return LiteralMixin in obj_or_cls.__bases__
    else:
        return LiteralMixin in obj_or_cls.__class__.__bases__


def is_collection(obj_or_cls) -> bool:
    if is_type(obj_or_cls):
        if issubclass(obj_or_cls, TfType):
            return issubclass(obj_or_cls, TfCollection)
        elif _is_supported_python_type(obj_or_cls):
            return issubclass(obj_or_cls, (list, set, dict))
        else:
            raise NotImplementedError
    else:
        if isinstance(obj_or_cls, TfType):
            return isinstance(obj_or_cls, TfCollection)
        elif _is_supported_python_obj(obj_or_cls):
            return isinstance(obj_or_cls, (list, set, dict))
        else:
            raise NotImplementedError


def is_hashable(obj) -> bool:
    try:
        _ = hash(obj)
        return True
    except TypeError:
        return False


def is_supported_python_obj_or_type(obj_or_cls) -> bool:
    if is_type(obj_or_cls):
        return _is_supported_python_type(obj_or_cls)
    else:
        return _is_supported_python_obj(obj_or_cls)


def _is_supported_python_obj(obj) -> bool:
    return _is_supported_python_type(obj.__class__)


def _is_supported_python_type(cls) -> bool:
    try:
        _ = _tftype_from_type_py(cls)
        return True
    except TerraformTypeError:
        return False


def _tftype_from_python_obj_or_type(obj_or_cls, deep: bool) -> Type[TfType]:
    if is_type(obj_or_cls):
        return _tftype_from_type_py(obj_or_cls)
    else:
        return _tftype_from_obj_py(obj_or_cls, deep)


def _tftype_from_obj_py(python_obj, deep: bool) -> TfTypeOutputType:
    if deep and is_collection(python_obj):
        tf_origin = _tftype_from_obj_py(python_obj, deep=False)
        tf_arg = _element_tftype_from_obj_py(python_obj, deep)
        return GenericAlias(tf_origin, (tf_arg,))
    else:
        return _tftype_from_type_py(python_obj.__class__)


def _element_tftype_from_obj_py(python_obj, deep: bool) -> TfTypeOutputType:
    if isinstance(python_obj, list):
        return _element_tftype_from_obj_py_list(python_obj, deep)
    elif isinstance(python_obj, dict):
        return _element_tftype_from_obj_py_dict(python_obj, deep)
    elif isinstance(python_obj, set):
        return _element_tftype_from_obj_py_set(python_obj, deep)
    else:
        raise TerraformTypeError(f'Cannot get element tftype of {repr(python_obj)}')


def _element_tftype_from_obj_py_list(python_list: List, deep: bool) -> TfTypeOutputType:
    if len(python_list) == 0:
        return TfUnknown
    else:
        return tftype(python_list[0], deep)


def _element_tftype_from_obj_py_dict(python_dict: Dict, deep: bool) -> TfTypeOutputType:
    if len(python_dict) == 0:
        return TfUnknown
    else:
        return tftype(next(iter(python_dict.values())), deep)


def _element_tftype_from_obj_py_set(python_set: Set, deep: bool) -> TfTypeOutputType:
    if len(python_set) == 0:
        return TfUnknown
    else:
        return tftype(next(iter(python_set)), deep)


def get_type_like(name: Union[str, list[str]]):
    """Get "type-like" from json type"""
    if isinstance(name, list):
        _types = tuple(map(get_type_like, name))
        return Union[_types]
    return {
        'bool': BoolLike,
        'null': NullLike,
        'number': NumberLike,
        'string': StringLike,
        'list': ListLike,
        'map': MapLike,
        'object': MapLike,
        'set': SetLike,
        'any': AnyLike,  # utility type
    }[name]


def get_element_tftype(obj, deep=False) -> Type[TfType]:
    if obj is None:
        return TfUnknown
    elif (
            hasattr(obj, 'element_type')
            and is_type_or_generic(obj.element_type)
    ):
        return tftype(getattr(obj, 'element_type'), deep)
    elif (
            hasattr(obj, 'data')
            and hasattr(obj.data, 'element_type')
            and is_type_or_generic(obj.data.element_type)
    ):
        return tftype(getattr(obj.data, 'element_type'), deep)
    elif isinstance(obj.data, list) and len(obj.data) > 0:
        return tftype(obj.data[0], deep)
    elif isinstance(obj.data, set) and len(obj.data) > 0:
        return tftype(next(iter(obj.data)), deep)
    elif isinstance(obj.data, dict) and len(obj.data) > 0:
        return tftype(next(iter(obj.data.values())), deep)
    elif isinstance(obj.data, deferred.Variable):
        var = obj.data
        if var.data.get('type') is None:
            return get_element_tftype(var.data.get('default'))
        else:
            return get_element_tftype(var.data.get('type'))
    elif isinstance(obj.data, deferred.Local):
        loc = obj.data
        return get_element_tftype(loc.value)
    elif is_generic(obj):
        return _get_element_type_from_generic(obj)
    return deferred.TfUnknown


def _get_element_type_from_generic(cls: Type) -> Type[TfType]:
    args = getattr(cls, '__args__')
    if len(args) == 1:
        return args[0]
    else:
        raise NotImplementedError


def is_instance(obj, cls):
    if isinstance(cls, tuple):
        return any(is_instance(obj, c) for c in cls)
    elif is_generic(obj) and is_generic(cls):
        return are_generics_equal(obj, cls)
    elif is_generic(obj):
        # cls is shallower than obj
        return is_instance(_tftype_from_generic(obj), cls)
    elif is_generic_union(cls):
        return any(is_instance(obj, c) for c in get_types_from_generic_union(cls))
    elif is_generic(cls):
        return (
                is_instance(obj, _tftype_from_generic(cls))
                and
                is_instance(obj.element_type(deep=True), get_element_type_from_generic(cls))
        )
    elif is_type(obj) and is_type(cls):
        return obj is cls
    else:
        return isinstance(obj, cls)


def are_generics_equal(left, right):
    if hasattr(left, '__origin__') and hasattr(right, '__origin__'):
        return (
                left.__origin__ == right.__origin__
                and len(left.__args__) == len(right.__args__)
                and all(are_generics_equal(left_arg, right_arg)
                        for left_arg, right_arg in
                        zip(left.__args__, right.__args__))
        )
    else:
        return left == right
