# internal
from .numeric import Numeric
from terraform_model.types import Number
from terraform_model.helpers.types import NumberLike, StringLike


class ParseInt(Numeric):

    def __init__(self, number: StringLike, base: NumberLike = 10):
        super().__init__('parseint', number, base)


def parseint(number: StringLike, base: NumberLike = 10) -> Number:
    return Number(ParseInt(number, base))
