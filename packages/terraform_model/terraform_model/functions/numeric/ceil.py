# internal
from terraform_model.functions.numeric.numeric import Numeric
from terraform_model.types import Number
from terraform_model.helpers.types import NumberLike


class Ceil(Numeric):

    def __init__(self, number: NumberLike):
        super().__init__('ceil', number)


def ceil(number: NumberLike) -> Number:
    return Number(Ceil(number))
