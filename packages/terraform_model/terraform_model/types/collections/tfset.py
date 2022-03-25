# std
from __future__ import annotations
from typing import Optional as Opt

# internal
from terraform_model.mixins import LiteralMixin
from terraform_model.types.collections.tfcollection import TfCollection, T
from terraform_model.utils.json import dumps
from terraform_model.mixins import ContainsMixin
from terraform_model.internal.deferred import deferred


class TfSet(TfCollection[T], ContainsMixin):

    def __str__(self) -> str:
        if isinstance(self.data, set):
            return dumps(list(self.data))
        else:
            return str(self.data)

    def __and__(self, other):
        return self.intersection(other)

    def __or__(self, other):
        return self.union(other)

    def __sub__(self, other):
        return self.subtract(other)

    def intersection(self, *others) -> TfSet:
        return deferred.tfsetintersection(self, *others)

    def subtract(self, other) -> TfSet:
        return deferred.tfsetsubtract(self, other)

    def union(self, *others) -> TfSet:
        return deferred.tfsetunion(self, *others)

    @classmethod
    def new(cls, data: Opt = None) -> TfSet:
        if data is None:
            return _empty
        elif isinstance(data, set):
            return TfSetLiteral(data)
        elif isinstance(data, (TfSet, TfSetLiteral)):
            return data
        else:
            return TfSet(data)


class TfSetLiteral(TfSet[T], LiteralMixin):

    def __init__(self, data: set):
        super().__init__(data)


def tfset(data: Opt = None) -> TfSet:
    return TfSet.new(data)


_empty = tfset(set())
