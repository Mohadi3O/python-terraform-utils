# std
from typing import cast, List, Union

# internal
from terraform_model.functions.collection.internal.collection_function import TfCollectionFunction
from terraform_model.types.conversions.typify import typify
from terraform_model.types import TfBool, TfList, TfString
from terraform_model.internal import tfassert

# types
TfAnyTrueClassInputType = Union[TfList[TfBool], TfList[TfString]]
TfAnyTrueFunctionInputType = Union[List[bool], List[str], TfList[TfBool], TfList[TfString]]


class TfAnyTrue(TfCollectionFunction):

    def __init__(self, list_input: TfAnyTrueClassInputType):
        tfassert.is_instance(list_input, TfAnyTrueClassInputType)
        super().__init__('anytrue', list_input)


def tfanytrue(list_input: TfAnyTrueFunctionInputType) -> TfBool:
    return TfBool(TfAnyTrue(cast(TfList, typify(list_input))))
