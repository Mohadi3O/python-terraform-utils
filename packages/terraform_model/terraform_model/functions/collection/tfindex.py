# std
from typing import cast

# internal
from terraform_model.functions.collection.internal.collection_function import TfCollectionFunction
from terraform_model.types.conversions.typify import typify
from terraform_model.types import tfnumber, TfList, TfNumber
from terraform_model.types.internal import TfType
from terraform_model.internal.tftype import ListLike, AnyLike
from terraform_model.internal import tfassert


class TfIndex(TfCollectionFunction):

    def __init__(self, list_input: TfList, value: TfType):
        tfassert.is_instance(list_input, TfList)
        tfassert.is_instance(value, TfType)
        tfassert.is_instance(value, list_input.element_type(deep=True))
        super().__init__('index', list_input, value)


def tfindex(list_input: ListLike, value: AnyLike) -> TfNumber:
    return tfnumber(TfIndex(cast(TfList, typify(list_input)), typify(value)))
