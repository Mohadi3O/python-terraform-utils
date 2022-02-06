# internal
from terraform_model.functions.numeric.numeric import Numeric
from terraform_model.types import Number
from terraform_model.helpers.types import NumberLike


class Log(Numeric):

    def __init__(self, number: NumberLike, base: NumberLike):
        super().__init__('log', number, base)


def log(number: NumberLike, base: NumberLike) -> Number:
    return Number(Log(number, base))
