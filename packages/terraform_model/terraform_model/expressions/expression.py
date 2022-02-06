from terraform_model.mixins import *
from terraform_model.types.typify import typify
from terraform_model.types.atomics.string import StringLiteral


class Expression(CompareMixin, ExpressionMixin, GetAttrMixin, GetItemMixin, MathMixin, ToMixin):

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
        if isinstance(arg, StringLiteral):
            return f'"{arg}"'
        else:
            return str(arg)
