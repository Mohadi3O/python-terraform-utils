# internal
from terraform_model.functions.numeric.internal.numeric_function import TfNumericFunction
from terraform_model.types import TfNumber
from terraform_model.internal.tftype import NumberLike


class TfLog(TfNumericFunction):

    def __init__(self, number: NumberLike, base: NumberLike):
        super().__init__('log', number, base)


def tflog(number: NumberLike, base: NumberLike) -> TfNumber:
    return TfNumber(TfLog(number, base))
