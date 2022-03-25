# internal
from terraform_model.functions.string._string import StringTfFunction
from terraform_model.types import *
from terraform_model.internal.tftype import StringLike


class TfRegexAll(StringTfFunction):

    def __init__(self, pattern: StringLike, string: StringLike):
        super().__init__('regexall', pattern, string)


def tfregexall(pattern: StringLike, string: StringLike) -> TfList:
    return TfList(TfRegexAll(pattern, string))
