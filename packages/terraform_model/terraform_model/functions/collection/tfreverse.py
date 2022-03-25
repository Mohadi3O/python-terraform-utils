# internal
from terraform_model.functions.collection.internal.collection_function import TfCollectionFunction
from terraform_model.types.conversions.typify import typify
from terraform_model.types import TfList
from terraform_model.internal.tftype import ListLike
from terraform_model.internal import tfassert


class TfReverse(TfCollectionFunction):

    def __init__(self, list_input: ListLike):
        list_input = typify(list_input)
        tfassert.is_instance(list_input, TfList)
        super().__init__('reverse', list_input)
        self.element_type = list_input.to_list().element_type()


def tfreverse(list_input: ListLike) -> TfList:
    return TfList(TfReverse(list_input))
