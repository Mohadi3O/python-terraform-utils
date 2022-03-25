from terraform_model.mixins import *
from terraform_model.types.conversions.typify import typify
from terraform_model.types.primitives.tfstring import TfStringLiteral


class Expression(CompareMixin, ExpressionMixin, GetItemMixin, MathMixin, ToMixin):

    def __init__(self, *args):
        self._args = list(map(typify, args))

    def __str__(self):
        if len(self._args) == 1:
            return str(self._args[0])
        else:
            return f'({" ".join(self.strings())})'

    def strings(self) -> list[str]:
        return list(map(self.str, self._args))

    @staticmethod
    def str(arg) -> str:
        return str(arg)
        # if isinstance(arg, TfStringLiteral):
        #     return f'"{arg}"'
        # else:
        #     return str(arg)
