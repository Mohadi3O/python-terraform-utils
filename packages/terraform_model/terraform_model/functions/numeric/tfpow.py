# internal
from terraform_model.functions.numeric.internal.numeric_function import TfNumericFunction
from terraform_model.types import TfNumber
from terraform_model.internal.tftype import NumberLike


class TfPow(TfNumericFunction):

    def __init__(self, number: NumberLike, exponent: NumberLike):
        super().__init__('pow', number, exponent)


def tfpow(number: NumberLike, exponent: NumberLike) -> TfNumber:
    return TfNumber(TfPow(number, exponent))
