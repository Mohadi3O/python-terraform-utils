# std
from typing import Union

# internal
from terraform_model.types.atomics.atomic import Atomic
from terraform_model.mixins import CompareMixin, LiteralMixin, MathMixin


class Number(Atomic, CompareMixin, MathMixin):

    def __str__(self):
        return str(self.data)


class NumberLiteral(Number, LiteralMixin):

    def __init__(self, data: Union[float, int]):
        super().__init__(data)
