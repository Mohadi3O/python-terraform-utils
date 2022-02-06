# internal
from terraform_model.functions.numeric.numeric import Numeric
from terraform_model.types import Number
from terraform_model.helpers.types import NumberLike


class SigNum(Numeric):

    def __init__(self, number: NumberLike):
        super().__init__('signum', number)


def signum(number: NumberLike) -> Number:
    return Number(SigNum(number))
