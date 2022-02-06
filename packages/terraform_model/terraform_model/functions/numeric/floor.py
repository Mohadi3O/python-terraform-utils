# internal
from terraform_model.functions.numeric.numeric import Numeric
from terraform_model.types import Number
from terraform_model.helpers.types import NumberLike


class Floor(Numeric):

    def __init__(self, number: NumberLike):
        super().__init__('floor', number)


def floor(number: NumberLike) -> Number:
    return Number(Floor(number))
