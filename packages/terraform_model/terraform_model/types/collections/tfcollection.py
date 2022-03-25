# std
from __future__ import annotations
from abc import abstractmethod
from typing import Generic, Type, TypeVar

# internal
from ...internal.deferred import deferred
from ..internal import TfType, TfUnknown
from ...internal import tfassert
from terraform_model.mixins import NonHashableMixin

# types
T = TypeVar('T', TfType, TfUnknown)


class TfCollection(TfType, Generic[T], NonHashableMixin):

    def __init__(self, data):
        if isinstance(data, list) and len(data) > 1:
            data = list(map(deferred.typify, data))
            tfassert.same_type(*data)
        elif isinstance(data, set) and len(data) > 1:
            data = set(map(deferred.typify, data))
            tfassert.same_type(*data)
        elif isinstance(data, dict) and len(data) > 1:
            data = dict(zip(data.keys(), map(deferred.typify, data.values())))
            tfassert.same_type(*data.values())
        super().__init__(data)

    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError

    def element_type(self, deep: bool = False) -> Type[TfType]:
        return deferred.tftype.get_element_tftype(self, deep=deep)
