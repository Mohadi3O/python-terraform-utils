# internal
from terraform_model.functions.string._string import StringTfFunction
from terraform_model.types import TfString
from terraform_model.internal.tftype import StringLike


class TfStrRev(StringTfFunction):

    def __init__(self, string: StringLike):
        super().__init__('strrev', string)


def tfstrrev(string: StringLike) -> TfString:
    return TfStrRev(string).to_string()
