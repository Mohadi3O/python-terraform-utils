# internal
from terraform_model.functions.string._string import StringTfFunction
from terraform_model.types import TfString
from terraform_model.internal.tftype import StringLike


class TfChomp(StringTfFunction):

    def __init__(self, string: StringLike):
        super().__init__('chomp', string)


def tfchomp(string: StringLike) -> TfString:
    return TfChomp(string).to_string()
