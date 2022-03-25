# std
from typing import cast, List, Union

# internal
from terraform_model.functions.collection.internal.collection_function import TfCollectionFunction
from terraform_model.types.conversions.typify import typify
from terraform_model.types import tflist, TfList, TfString
from terraform_model.internal import tfassert


class TfSort(TfCollectionFunction):
    element_type = TfString

    def __init__(self, list_input: TfList[TfString]):
        tfassert.is_instance(list_input, TfList)
        tfassert.element_type_is(list_input, TfString)
        super().__init__('sort', list_input)


def tfsort(list_input: Union[List[str], List[TfString], TfList[TfString]]) -> TfList[TfString]:
    return tflist(TfSort(cast(TfList, typify(list_input))))
