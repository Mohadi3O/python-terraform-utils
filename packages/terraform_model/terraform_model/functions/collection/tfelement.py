# internal
from terraform_model.functions.collection.internal.collection_function import TfCollectionFunction
from terraform_model.types.conversions.typify import typify
from terraform_model.types import TfList, TfNumber
from terraform_model.types.internal import TfType
from terraform_model.internal.tftype import NumberLike, ListLike


class TfElement(TfCollectionFunction):

    def __init__(self, list_input: TfList, index: TfNumber):
        super().__init__('element', list_input, index)


def tfelement(list_input: ListLike, index: NumberLike) -> TfType:
    list_input = typify(list_input).to_list()
    index = typify(index).to_number()
    element_type = list_input.element_type()
    return element_type.new(TfElement(list_input, index))
