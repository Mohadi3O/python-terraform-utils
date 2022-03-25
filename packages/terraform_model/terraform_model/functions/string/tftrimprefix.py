# internal
from terraform_model.functions.string._string import StringTfFunction
from terraform_model.types import TfString
from terraform_model.internal.tftype import StringLike


class TfTrimPrefix(StringTfFunction):

    def __init__(self, string: StringLike, prefix: StringLike):
        super().__init__('trimprefix', string, prefix)


def tftrimprefix(string: StringLike, prefix: StringLike) -> TfString:
    return TfTrimPrefix(string, prefix).to_string()
