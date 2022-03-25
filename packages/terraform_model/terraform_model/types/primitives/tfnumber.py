# std
from __future__ import annotations
from typing import Optional as Opt, Union

# internal
from terraform_model.types.primitives.tfprimitive import TfPrimitive
from terraform_model.mixins import CompareMixin, LiteralMixin, MathMixin


class TfNumber(TfPrimitive, CompareMixin, MathMixin):

    def __str__(self):
        return str(self.data)

    @classmethod
    def new(cls, data: Opt = None) -> TfNumber:
        if data is None:
            return _empty
        elif isinstance(data, (float, int, TfNumberLiteral)):
            return TfNumberLiteral(data)
        else:
            return TfNumber(data)


class TfNumberLiteral(TfNumber, LiteralMixin):

    def __init__(self, data: Union[float, int]):
        super().__init__(data)


def tfnumber(data: Opt = None) -> TfNumber:
    return TfNumber.new(data)


_empty = tfnumber(0)
