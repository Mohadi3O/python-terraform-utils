# std
from typing import cast

# internal
from terraform_model.functions.collection.internal.collection_function import TfCollectionFunction
from terraform_model.types.conversions.typify import typify
from terraform_model.types import tflist, TfList
from terraform_model.internal.tftype import ListLike
from terraform_model.internal import tfassert


class TfDistinct(TfCollectionFunction):

    def __init__(self, list_input: TfList):
        tfassert.is_instance(list_input, TfList)
        super().__init__('distinct', list_input)
        self.element_type = list_input.element_type(deep=True)


def tfdistinct(list_input: ListLike) -> TfList:
    return tflist(TfDistinct(cast(TfList, typify(list_input))))
