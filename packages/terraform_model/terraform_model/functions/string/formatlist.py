# internal
from terraform_model.functions.string.string_function import StringFunction
from terraform_model.types import String
from terraform_model.helpers.types import StringLike, AnyLike


class FormatList(StringFunction):

    def __init__(self, spec: StringLike, *values: AnyLike):
        super().__init__('formatlist', spec, *values)


def formatlist(spec: StringLike, *values: AnyLike) -> String:
    return String(FormatList(spec, *values))
