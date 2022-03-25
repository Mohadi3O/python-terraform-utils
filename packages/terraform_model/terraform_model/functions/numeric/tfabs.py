# std
from terraform_model.functions.numeric.internal.numeric_function import TfNumericFunction
from terraform_model.types import TfNumber
from terraform_model.internal.tftype import NumberLike


class TfAbs(TfNumericFunction):

    def __init__(self, number: NumberLike):
        super().__init__('abs', number)


def tfabs(number: NumberLike) -> TfNumber:
    return TfNumber(TfAbs(number))
