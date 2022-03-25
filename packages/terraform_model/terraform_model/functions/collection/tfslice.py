# std
from typing import cast, Optional as Opt

# internal
from terraform_model.functions.collection.internal.collection_function import TfCollectionFunction
from terraform_model.types.conversions.typify import typify
from terraform_model.types import TfList, tfnumber, TfNumber
from ...internal.tftype import NumberLike, ListLike
from ...internal import tfassert
from .tflength import tflength


class TfSlice(TfCollectionFunction):

    def __init__(self, list_input: TfList, start_index: TfNumber, end_index: TfNumber):
        tfassert.is_instance(list_input, TfList)
        tfassert.all_is_instance(TfNumber, start_index, end_index)
        super().__init__('slice', list_input, start_index, end_index)
        self.element_type = list_input.element_type()


def tfslice(
        list_input: ListLike,
        start_index: Opt[NumberLike] = None,
        end_index: Opt[NumberLike] = None,
) -> TfList:
    list_input = cast(TfList, typify(list_input))
    start_index = tfnumber(0) if start_index is None else cast(TfNumber, typify(start_index))
    end_index = tflength(list_input) if end_index is None else cast(TfNumber, typify(end_index))
    return TfList(TfSlice(list_input, start_index, end_index))
