# internal
from terraform_model.functions.string._string import StringTfFunction
from terraform_model.types import TfString
from terraform_model.internal.tftype import StringLike


class TfTrim(StringTfFunction):

    def __init__(self, string: StringLike, str_character_set: StringLike):
        super().__init__('trim', string, str_character_set)


def tftrim(string: StringLike, str_character_set: StringLike = ' ') -> TfString:
    return TfTrim(string, str_character_set).to_string()
