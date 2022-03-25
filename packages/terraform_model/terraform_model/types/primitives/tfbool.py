# std
from typing import Optional as Opt

# internal
from terraform_model.types.primitives.tfprimitive import TfPrimitive
from terraform_model.mixins import CompareMixin, LiteralMixin, LogicalMixin


class TfBool(TfPrimitive, CompareMixin, LogicalMixin):

    def __str__(self):
        if isinstance(self.data, bool):
            return 'true' if self.data else 'false'
        else:
            return str(self.data)

    @classmethod
    def new(cls, data: Opt = None):
        data = false if data is None else data
        if data is true or data is True:
            return true
        elif data is false or data is False:
            return false
        else:
            return TfBool(data)


class TfBoolLiteral(TfBool, LiteralMixin):

    def __init__(self, data: bool):
        super().__init__(data)

    def __str__(self):
        return 'true' if self.data else 'false'


def tfbool(data: Opt = None) -> TfBool:
    return TfBool.new(data)


true = TfBoolLiteral(True)
false = TfBoolLiteral(False)
