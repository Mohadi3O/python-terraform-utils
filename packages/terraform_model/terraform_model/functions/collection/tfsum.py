# std
from typing import cast, Union

# internal
from terraform_model.functions.collection.internal.collection_function import TfCollectionFunction
from terraform_model.types.conversions.typify import typify
from terraform_model.types import tfnumber, TfList, TfNumber, TfSet
from terraform_model.internal.tftype import ListLike, SetLike
from terraform_model.internal import tfassert

# types
TfSumFunctionInputType = Union[ListLike, SetLike]
TfSumClassInputType = Union[TfList, TfSet]


class TfSum(TfCollectionFunction):

    def __init__(self, list_or_set: TfSumClassInputType):
        tfassert.is_instance(list_or_set, (TfList, TfSet))
        tfassert.element_type_is(list_or_set, TfNumber)
        super().__init__('sum', list_or_set)


def tfsum(list_or_set: TfSumFunctionInputType) -> TfNumber:
    return tfnumber(TfSum(cast(TfSumClassInputType, typify(list_or_set))))
