# internal
from terraform_model.functions.string.string_function import StringFunction
from terraform_model.types import String


class Lower(StringFunction):

    def __init__(self, string: String):
        super().__init__('join', string)
