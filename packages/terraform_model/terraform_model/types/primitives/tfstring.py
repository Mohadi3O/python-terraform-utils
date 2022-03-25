# std
from __future__ import annotations
from typing import Optional as Opt

# internal
from terraform_model.types.primitives.tfprimitive import TfPrimitive
from terraform_model.mixins import LengthMixin, LiteralMixin


class TfString(TfPrimitive, LengthMixin):

    def __str__(self):
        if isinstance(self.data, str):
            return f'"{self.data}"'
        else:
            return str(self.data)

    @classmethod
    def new(cls, data: Opt = None) -> TfString:
        if data is None:
            return _empty
        elif isinstance(data, (str, TfStringLiteral)):
            return TfStringLiteral(data)
        else:
            return TfString(data)


class TfStringLiteral(TfString, LiteralMixin):

    def __init__(self, data: str):
        super().__init__(data)


def tfstring(data: Opt = None) -> TfString:
    return TfString.new(data)


_empty = tfstring('')
