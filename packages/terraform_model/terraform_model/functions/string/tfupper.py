# internal
from terraform_model.functions.string._string import StringTfFunction
from terraform_model.types import TfString
from terraform_model.internal.tftype import StringLike


class TfUpper(StringTfFunction):

    def __init__(self, string: StringLike):
        super().__init__('upper', string)


def tfupper(string: StringLike) -> TfString:
    return TfUpper(string).to_string()
