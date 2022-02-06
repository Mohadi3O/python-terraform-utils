# internal
from terraform_model.functions.string.string_function import StringFunction
from terraform_model.types import String
from terraform_model.helpers.types import NumberLike, StringLike


class Indent(StringFunction):

    def __init__(self, num_spaces: NumberLike, string: StringLike):
        super().__init__('indent', num_spaces, string)


def indent(num_spaces: NumberLike, string: StringLike) -> String:
    return String(Indent(num_spaces, string))
