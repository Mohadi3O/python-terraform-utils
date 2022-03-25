# internal
from terraform_model.functions.string._string import StringTfFunction
from terraform_model.types import TfString
from terraform_model.internal.tftype import StringLike


class TfTrimSpace(StringTfFunction):

    def __init__(self, string: StringLike):
        super().__init__('trimspace', string)


def tftrimspace(string: StringLike) -> TfString:
    return TfTrimSpace(string).to_string()
