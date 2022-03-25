# internal
from terraform_model.functions.string._string import StringTfFunction
from terraform_model.types import TfString
from terraform_model.internal.tftype import StringLike, ListLike


class TfJoin(StringTfFunction):

    def __init__(self, separator: StringLike, items: ListLike):
        super().__init__('join', separator, items)


def tfjoin(separator: StringLike, items: ListLike) -> TfString:
    return TfString(TfJoin(separator, items))
