# std
from typing import Optional as Opt

# internal
from terraform_model.types.primitives.tfprimitive import TfPrimitive
from terraform_model.mixins.literal import LiteralMixin


class TfNull(TfPrimitive):

    def __init__(self, data):
        super().__init__(data)

    def __str__(self):
        return 'null'

    @classmethod
    def new(cls, data: Opt = None):
        if data is None or data is null:
            return null
        else:
            return TfNull(data)


class TfNullLiteral(TfNull, LiteralMixin):

    def __init__(self):
        super().__init__(None)


def tfnull(data: Opt = None) -> TfNull:
    return TfNull.new(data)


null = TfNullLiteral()
