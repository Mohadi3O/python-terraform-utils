# internal
from terraform_model.functions.string._string import StringTfFunction
from terraform_model.types import TfString
from terraform_model.internal.tftype import StringLike, NumberLike


class TfIndent(StringTfFunction):

    def __init__(self, num_spaces: NumberLike, string: StringLike):
        super().__init__('indent', num_spaces, string)


def tfindent(num_spaces: NumberLike, string: StringLike) -> TfString:
    return TfString(TfIndent(num_spaces, string))
