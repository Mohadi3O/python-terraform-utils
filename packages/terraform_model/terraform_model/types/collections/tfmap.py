# std
from __future__ import annotations
from typing import Optional as Opt, Union

# internal
from terraform_model.types.collections.tfcollection import TfCollection, T
from terraform_model.utils.json import dumps
from terraform_model.mixins import GetItemMixin, LengthMixin, LiteralMixin
from .tflist import TfList
from ..primitives import TfString
from terraform_model.internal.deferred import deferred


class TfMap(TfCollection[T], GetItemMixin, LengthMixin):

    def __str__(self) -> str:
        if isinstance(self.data, dict):
            return dumps(self.data)
        else:
            return str(self.data)

    def __add__(self, other: Union[dict, TfMap]):
        return self.merge(other)

    def keys(self) -> TfList[TfString]:
        return deferred.tfkeys(self)

    def values(self) -> TfList[T]:
        return deferred.tfvalues(self)

    def lookup(self, key: Union[str, TfString], default: T) -> T:
        return deferred.tflookup(self, key, default)

    def merge(self, *maps: Union[dict, TfMap]) -> TfMap[T]:
        return deferred.tfmerge(self, *maps)

    @classmethod
    def new(cls, data: Opt = None) -> TfMap:
        if data is None:
            return _empty
        elif isinstance(data, dict):
            return TfMapLiteral(data)
        elif isinstance(data, (TfMap, TfMapLiteral)):
            return data
        else:
            return TfMap(data)


class TfMapLiteral(TfMap[T], LiteralMixin):

    def __init__(self, data: dict):
        super().__init__(data)


def tfmap(data: Opt = None) -> TfMap:
    return TfMap.new(data)


_empty = tfmap({})
