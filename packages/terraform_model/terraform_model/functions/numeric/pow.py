# internal
from terraform_model.functions.numeric.numeric import Numeric
from terraform_model.types import Number
from terraform_model.helpers.types import NumberLike


class Pow(Numeric):

    def __init__(self, number: NumberLike, exponent: NumberLike):
        super().__init__('pow', number, exponent)


def pow_(number: NumberLike, exponent: NumberLike) -> Number:
    return Number(Pow(number, exponent))
