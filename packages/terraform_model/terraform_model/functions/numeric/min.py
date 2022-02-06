# internal
from terraform_model.functions.numeric.numeric import Numeric
from terraform_model.types import Number
from terraform_model.helpers.types import NumberLike


class Min(Numeric):

    def __init__(self, *numbers: NumberLike):
        super().__init__('min', *numbers)


def min_(*numbers: NumberLike) -> Number:
    return Number(Min(*numbers))
