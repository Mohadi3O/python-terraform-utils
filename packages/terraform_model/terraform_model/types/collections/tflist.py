# std
from __future__ import annotations
from typing import Optional as Opt, Union

# internal
from terraform_model.types.primitives.tfstring import TfString
from terraform_model.types.primitives.tfnumber import TfNumber
from terraform_model.types.collections.tfcollection import TfCollection, T
from terraform_model.utils.json import dumps
from terraform_model.mixins import ContainsMixin, LengthMixin, LiteralMixin
from terraform_model.internal.deferred import deferred


class TfList(TfCollection[T], ContainsMixin, LengthMixin):

    def __str__(self) -> str:
        if isinstance(self.data, list):
            return dumps(self.data)
        else:
            return str(self.data)

    def __getitem__(self, item):
        if isinstance(item, slice):
            return self.slice(item.start, item.stop)
        else:
            return deferred.index(self, item)

    def __add__(self, other: Union[list[T], TfList[T]]) -> TfList[T]:
        return self.concat(other)

    def chunk(self, n: Union[int, TfNumber]) -> TfList[T]:
        return deferred.tfchunklist(self, n)

    def concat(self, *lists: Union[list[T], TfList[T]]) -> TfList[T]:
        return deferred.tfconcat(self, *lists)

    def distinct(self) -> TfList[T]:
        return deferred.tfdistinct(self)

    def element(self, index: Union[int, TfNumber]) -> T:
        return deferred.tfelement(self, index)

    def index(self, item: T) -> TfNumber:
        return deferred.tfindex(self, item)

    def reverse(self) -> TfList[T]:
        return deferred.tfreverse(self)

    def slice(
            self,
            start: Opt[Union[int, TfNumber]] = None,
            end: Opt[Union[int, TfNumber]] = None
    ) -> TfList[T]:
        return deferred.tfslice(self, start_index=start, end_index=end)

    def sort(self) -> TfList[TfString]:
        return deferred.tfsort(self)

    @classmethod
    def new(cls, data: Opt = None) -> TfList:
        if data is None:
            return _empty
        elif isinstance(data, list):
            return TfListLiteral(data)
        elif isinstance(data, (TfList, TfListLiteral)):
            return data
        else:
            return TfList(data)


class TfListLiteral(TfList[T], LiteralMixin):

    def __init__(self, data: list):
        super().__init__(data)


def tflist(data) -> TfList:
    return TfList.new(data)


_empty = tflist([])
