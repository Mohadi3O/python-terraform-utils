# internal
from terraform_model.functions.string._string import StringTfFunction
from terraform_model.types import TfString
from terraform_model.internal.tftype import StringLike


class TfTrimSuffix(StringTfFunction):

    def __init__(self, string: StringLike, suffix: StringLike):
        super().__init__('trimsuffix', string, suffix)


def tftrimsuffix(string: StringLike, suffix: StringLike) -> TfString:
    return TfTrimSuffix(string, suffix).to_string()
