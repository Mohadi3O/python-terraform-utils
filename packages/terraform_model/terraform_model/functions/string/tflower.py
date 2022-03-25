# internal
from terraform_model.functions.string._string import StringTfFunction
from terraform_model.types import TfString
from terraform_model.internal.tftype import StringLike


class TfLower(StringTfFunction):

    def __init__(self, string: StringLike):
        super().__init__('lower', string)


def tflower(string: StringLike) -> TfString:
    return TfString(TfLower(string))
