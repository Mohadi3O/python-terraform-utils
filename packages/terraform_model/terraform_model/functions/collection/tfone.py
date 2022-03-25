# std
from typing import cast, Union

# internal
from terraform_model.functions.collection.internal.collection_function import TfCollectionFunction
from terraform_model.types.conversions.typify import typify
from terraform_model.types import TfList, TfSet, TfTuple
from terraform_model.types.internal import tfunknown, TfType
from terraform_model.internal.tftype import ListLike, SetLike, TupleLike

# types
TfOneClassInputType = Union[TfList, TfSet, TfTuple]
TfOneFunctionInputType = Union[ListLike, SetLike, TupleLike]


class TfOne(TfCollectionFunction):

    def __init__(self, list_or_set_or_tuple: TfOneClassInputType):
        super().__init__('one', list_or_set_or_tuple)


def tfone(list_or_set_or_tuple: TfOneFunctionInputType) -> TfType:
    list_or_set_or_tuple = cast(TfOneClassInputType, typify(list_or_set_or_tuple))
    return list_or_set_or_tuple.element_type().new(TfOne(list_or_set_or_tuple))
