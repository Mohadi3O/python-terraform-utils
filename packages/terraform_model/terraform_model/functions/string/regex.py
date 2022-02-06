# internal
from terraform_model.functions.string.string_function import StringFunction
from terraform_model.types import String


class Regex(StringFunction):

    def __init__(self, pattern: String, string: String):
        super().__init__('regex', pattern, string)
