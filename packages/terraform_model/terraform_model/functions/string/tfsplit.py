# internal
from terraform_model.functions.string._string import StringTfFunction
from terraform_model.types import TfList
from terraform_model.internal.tftype import StringLike, ListLike


class TfSplit(StringTfFunction):

    def __init__(self, separator: StringLike, items: ListLike):
        super().__init__('split', separator, items)


def tfsplit(separator: StringLike, items: ListLike) -> TfList:
    return TfList(TfSplit(separator, items))
