# std
from typing import cast, Union

# internal
from terraform_model.functions.collection.internal.collection_function import TfCollectionFunction
from terraform_model.types.conversions.typify import typify
from terraform_model.types import tfnumber, TfList, TfMap, TfNumber, TfString
from terraform_model.internal.tftype import StringLike, ListLike, MapLike
from terraform_model.internal import tfassert

# types
LengthClassInputType = Union[TfList, TfMap, TfString]
LengthFunctionInputType = Union[ListLike, MapLike, StringLike]


class TfLength(TfCollectionFunction):

    def __init__(self, length_input: LengthFunctionInputType):
        tfassert.is_instance(length_input, LengthClassInputType)
        super().__init__('length', length_input)


def tflength(length_input: LengthFunctionInputType) -> TfNumber:
    return tfnumber(TfLength(cast(LengthClassInputType, typify(length_input))))
