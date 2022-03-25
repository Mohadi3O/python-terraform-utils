# std
from typing import cast, Dict, List, Union

# internal
from terraform_model.functions.collection.internal.collection_function import TfCollectionFunction
from terraform_model.types.conversions.typify import typify
from terraform_model.types import tfmap, TfList, TfMap, TfString
from terraform_model.internal import tfassert

# types
TfTransposeClassInputType = TfMap[TfList[TfString]]
TfTransposeFunctionInputType = Union[Dict[str, List[str]], TfTransposeClassInputType]
TfTransposeClassOutputType = TfMap[TfList[TfString]]


class TfTranspose(TfCollectionFunction):
    element_type = TfList[TfString]

    def __init__(self, list_or_set: TfTransposeClassInputType):
        tfassert.is_instance(list_or_set, TfTransposeClassInputType)
        super().__init__('transpose', list_or_set)


def tftranspose(map_of_lists_of_strings: TfTransposeFunctionInputType) -> TfTransposeClassOutputType:
    return tfmap(TfTranspose(cast(TfTransposeClassInputType, typify(map_of_lists_of_strings))))
