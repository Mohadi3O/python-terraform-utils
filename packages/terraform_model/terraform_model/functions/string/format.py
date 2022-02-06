# internal
from terraform_model.functions.string.string_function import StringFunction
from terraform_model.types import String
from terraform_model.helpers.types import StringLike, AnyLike


class Format(StringFunction):

    def __init__(self, spec: StringLike, *values: AnyLike):
        super().__init__('format', spec, *values)


def format_(spec: StringLike, *values: AnyLike) -> String:
    return String(Format(spec, *values))
