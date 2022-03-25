# std
from typing import cast

# internal
from terraform_model.functions.collection.internal.collection_function import TfCollectionFunction
from terraform_model.types.conversions.typify import typify
from terraform_model.types import tflist, TfList
from terraform_model.internal.tftype import ListLike
from terraform_model.internal import tfassert


class TfFlatten(TfCollectionFunction):

    def __init__(self, list_input: TfList):
        tfassert.is_instance(list_input, TfList)
        super().__init__('flatten', list_input)


def tfflatten(list_input: ListLike) -> TfList:
    return tflist(TfFlatten(cast(TfList, typify(list_input))))
