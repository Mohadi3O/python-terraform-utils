# internal
from terraform_model.functions.string.string_function import StringFunction
from terraform_model.types import String
from terraform_model.helpers.types import StringLike, ListLike


class Join(StringFunction):

    def __init__(self, separator: StringLike, items: ListLike):
        super().__init__('join', separator, items)


def join(separator: StringLike, items: ListLike) -> String:
    return String(Join(separator, items))
