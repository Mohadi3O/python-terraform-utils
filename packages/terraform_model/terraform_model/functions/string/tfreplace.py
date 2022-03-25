# internal
from terraform_model.functions.string._string import StringTfFunction
from terraform_model.types import TfString
from terraform_model.internal.tftype import StringLike


class TfReplace(StringTfFunction):

    def __init__(self, string: StringLike, substring: StringLike, replacement: StringLike):
        super().__init__('replace', string, substring, replacement)


def tfreplace(string: StringLike, substring: StringLike, replacement: StringLike) -> TfString:
    return TfString(TfReplace(string, substring, replacement))
