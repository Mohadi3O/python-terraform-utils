# internal
from terraform_model.functions.numeric.internal.numeric_function import TfNumericFunction
from terraform_model.types import TfNumber
from terraform_model.internal.tftype import NumberLike


class TfSigNum(TfNumericFunction):

    def __init__(self, number: NumberLike):
        super().__init__('signum', number)


def tfsignum(number: NumberLike) -> TfNumber:
    return TfNumber(TfSigNum(number))
