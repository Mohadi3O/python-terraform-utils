# internal
from terraform_model.functions.string._string import StringTfFunction
from terraform_model.types import TfString
from terraform_model.internal.tftype import StringLike, NumberLike


class TfSubStr(StringTfFunction):

    def __init__(self, string: StringLike, offset: NumberLike, length: NumberLike):
        super().__init__('substr', string, offset, length)


def tfsubstr(string: StringLike, offset: NumberLike, length: NumberLike) -> TfString:
    return TfSubStr(string, offset, length).to_string()
