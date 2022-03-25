# std
from inspect import Parameter, Signature
import json
from typing import Optional as Opt, Union

# internal
from ..internal.tftype import TfType
from ..primitives import TfPrimitive, TfBool, TfNull, TfNumber, TfString
from ..collections import TfCollection, TfList, TfMap, TfSet
from ..structurals import TfStructural, TfTuple, TfObject
from terraform_model.expressions.expressions.getattr import GetAttr
from terraform_model.utils.utils import get_class_name

# types
_definition_str = str
_definition_list = list
_definition_type = Union[_definition_str, _definition_list]


def structify(definition: _definition_type, name: Opt[str] = None) -> type(TfStructural):
    if isinstance(definition, str):
        if _is_primitive(definition):
            return _structify_primitive(definition)
        else:
            raise NotImplementedError
    elif isinstance(definition, list):
        if _is_collection(definition):
            return _structify_collection(definition)
        elif _is_object(definition):
            return _structify_object(definition, name)
        elif _is_tuple(definition):
            return _structify_tuple(definition)
        else:
            raise NotImplementedError
    else:
        raise NotImplementedError


_primitive_mapping = {
    'null': TfNull,
    'bool': TfBool,
    'number': TfNumber,
    'string': TfString,
}


def _is_primitive(definition: _definition_str) -> bool:
    return definition in _primitive_mapping.keys()


def _structify_primitive(definition: _definition_str) -> type(TfPrimitive):
    return _primitive_mapping[definition]


_collection_mapping = {
    'list': TfList,
    'map': TfMap,
    'set': TfSet,
}


def _is_collection(definition: _definition_list) -> bool:
    return definition[0] in _collection_mapping.keys()


def _structify_collection(definition: _definition_list) -> type(TfCollection):
    return _collection_mapping[definition[0]][structify(definition[1])]


def _is_object(definition: _definition_list) -> bool:
    return definition[0] == 'object'


def _structify_object(definition: _definition_list, name: Opt[str] = None) -> type(TfObject):
    name = f'TfObject{abs(hash(json.dumps(definition)))}' if name is None else get_class_name(name)
    obj_dict = {}

    def prop(name: str, tf_type: type(TfType)):
        def _prop(self):
            if isinstance(self._data, dict):
                return tf_type(self._data[name])
            else:
                return tf_type(GetAttr(self, name))

        return _prop

    for k, v in definition[1].items():
        K = get_class_name(k)
        V = structify(v)
        obj_dict[K] = V
        obj_dict[k] = property(prop(k, V))
    obj_dict['__definition__'] = definition
    return type(name, (TfObject,), obj_dict)


def _is_tuple(definition: _definition_list) -> bool:
    return definition[0] == 'tuple'


def _structify_tuple(definition: _definition_list, name: Opt[str] = None) -> type(TfTuple):
    raise NotImplementedError
