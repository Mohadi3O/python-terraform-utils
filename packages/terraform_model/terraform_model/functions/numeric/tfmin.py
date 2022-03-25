# internal
from terraform_model.functions.numeric.internal.numeric_function import TfNumericFunction
from terraform_model.types import TfNumber
from terraform_model.internal.tftype import NumberLike


class TfMin(TfNumericFunction):

    def __init__(self, *numbers: NumberLike):
        super().__init__('min', *numbers)


def tfmin(*numbers: NumberLike) -> TfNumber:
    return TfNumber(TfMin(*numbers))
