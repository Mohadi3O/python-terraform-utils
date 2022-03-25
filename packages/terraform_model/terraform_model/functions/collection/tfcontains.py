# std
from typing import cast, Union

# internal
from terraform_model.functions.collection.internal.collection_function import TfCollectionFunction
from terraform_model.types.conversions.typify import typify
from terraform_model.types import tfbool, TfBool, TfList, TfSet
from terraform_model.types.internal import TfType
from terraform_model.internal.tftype import ListLike, AnyLike, SetLike
from terraform_model.internal import tfassert


class TfContains(TfCollectionFunction):

    def __init__(self, list_or_set: Union[TfList, TfSet], value: TfType):
        tfassert.is_instance(list_or_set, Union[TfList, TfSet])
        tfassert.is_instance(value, TfType)
        tfassert.is_instance(value, list_or_set.element_type(deep=True))
        super().__init__('contains', list_or_set, value)


def tfcontains(list_or_set: Union[ListLike, SetLike], value: AnyLike) -> TfBool:
    result = tfbool(TfContains(cast(Union[TfList, TfSet], typify(list_or_set)), typify(value)))
    return result
