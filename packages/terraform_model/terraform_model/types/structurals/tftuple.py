# std
from __future__ import annotations
from typing import Optional as Opt

# internal
from terraform_model.types.structurals.tfstructural import TfStructural
from terraform_model.utils.json import dumps
from terraform_model.mixins.literal import LiteralMixin


class TfTuple(TfStructural):

    def __init__(self, data: Opt = None):
        super().__init__(data)

    def __str__(self) -> str:
        if isinstance(self.data, tuple):
            return dumps(self.data)
        else:
            return str(self.data)

    @classmethod
    def new(cls, data: Opt = None) -> TfTuple:
        if data is None:
            return _empty
        elif isinstance(data, tuple):
            return TfTupleLiteral(data)
        else:
            return TfTuple(data)


class TfTupleLiteral(TfTuple, LiteralMixin):

    def __init__(self, data: tuple):
        super().__init__(data)


def tftuple(data: Opt = None) -> TfTuple:
    return TfTuple.new(data)


_empty = tftuple(tuple())
