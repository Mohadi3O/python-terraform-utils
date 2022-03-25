# internal
from terraform_model.functions.numeric.internal.numeric_function import TfNumericFunction
from terraform_model.types import TfNumber
from terraform_model.internal.tftype import StringLike, NumberLike


class TfParseInt(TfNumericFunction):

    def __init__(self, number: StringLike, base: NumberLike = 10):
        super().__init__('parseint', number, base)


def tfparseint(number: StringLike, base: NumberLike = 10) -> TfNumber:
    return TfNumber(TfParseInt(number, base))
