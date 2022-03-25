# std
from typing import cast, Generic, List, TypeVar, Union

# internal
from terraform_model.functions.collection.internal.collection_function import TfCollectionFunction
from terraform_model.types.conversions.typify import typify
from terraform_model.types import TfList, TfNumber
from terraform_model.internal.tftype import NumberLike
from terraform_model.internal import tfassert

# types
T = TypeVar('T')


class TfChunkList(TfCollectionFunction, Generic[T]):

    def __init__(self, list_input: TfList[T], chunk_size: TfNumber):
        tfassert.is_instance(list_input, TfList)
        tfassert.is_instance(chunk_size, TfNumber)
        super().__init__('chunklist', list_input, chunk_size)
        self.element_type = TfList[list_input.element_type()]


def tfchunklist(list_input: Union[List[T], TfList[T]], chunk_size: NumberLike) -> TfList[TfList[T]]:
    list_input = cast(TfList, typify(list_input))
    chunk_size = cast(TfNumber, typify(chunk_size))
    return TfList(TfChunkList(list_input, chunk_size))
