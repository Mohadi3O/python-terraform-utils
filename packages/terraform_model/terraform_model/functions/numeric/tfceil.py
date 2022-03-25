# internal
from terraform_model.functions.numeric.internal.numeric_function import TfNumericFunction
from terraform_model.types import TfNumber
from terraform_model.internal.tftype import NumberLike


class TfCeil(TfNumericFunction):

    def __init__(self, number: NumberLike):
        super().__init__('ceil', number)


def tfceil(number: NumberLike) -> TfNumber:
    return TfNumber(TfCeil(number))
