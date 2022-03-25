# std
from typing import cast, List, Union

# internal
from terraform_model.functions.collection.internal.collection_function import TfCollectionFunction
from terraform_model.types.conversions.typify import typify
from terraform_model.types import TfBool, TfList, TfString
from terraform_model.internal import tfassert

# types
TfAllTrueClassInputType = Union[TfList[TfBool], TfList[TfString]]
TfAllTrueFunctionInputType = Union[List[bool], List[str], TfList[TfBool], TfList[TfString]]


class TfAllTrue(TfCollectionFunction):

    def __init__(self, list_input: TfAllTrueClassInputType):
        tfassert.is_instance(list_input, TfAllTrueClassInputType)
        super().__init__('alltrue', list_input)


def tfalltrue(list_input: TfAllTrueFunctionInputType) -> TfBool:
    return TfBool(TfAllTrue(cast(TfList, typify(list_input))))
