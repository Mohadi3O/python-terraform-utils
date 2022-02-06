# std
from terraform_model.functions.numeric.numeric import Numeric
from terraform_model.types import Number
from terraform_model.helpers.types import NumberLike


class Abs(Numeric):

    def __init__(self, number: NumberLike):
        super().__init__('abs', number)


def abs_(number: NumberLike) -> Number:
    return Number(Abs(number))
