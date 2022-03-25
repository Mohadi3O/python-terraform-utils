# internal
from terraform_model.functions.string._string import StringTfFunction
from terraform_model.types import TfString
from terraform_model.internal.tftype import StringLike


class TfTitle(StringTfFunction):

    def __init__(self, string: StringLike):
        super().__init__('title', string)


def tftitle(string: StringLike) -> TfString:
    return TfTitle(string).to_string()
