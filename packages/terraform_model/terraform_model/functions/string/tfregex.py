# internal
from terraform_model.functions.string._string import StringTfFunction
from terraform_model.types.internal import tfunknown, TfUnknown
from terraform_model.internal.tftype import StringLike


class TfRegex(StringTfFunction):

    def __init__(self, pattern: StringLike, string: StringLike):
        super().__init__('regex', pattern, string)


def tfregex(pattern: StringLike, string: StringLike) -> TfUnknown:
    return tfunknown(TfRegex(pattern, string))
