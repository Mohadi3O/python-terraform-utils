# internal
from terraform_model.functions.string.string_function import StringFunction
from terraform_model.types import String
from terraform_model.helpers.types import StringLike


class Chomp(StringFunction):

    def __init__(self, string: StringLike):
        super().__init__('chomp', string)


def chomp(string: StringLike) -> String:
    return String(Chomp(string))
