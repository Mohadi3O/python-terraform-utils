# std
from typing import cast

# internal
from terraform_model.functions.collection.internal.collection_function import TfCollectionFunction
from terraform_model.types.conversions.typify import typify
from terraform_model.types import tflist, TfList, TfMap
from terraform_model.internal.tftype import MapLike
from terraform_model.internal import tfassert


class TfValues(TfCollectionFunction):

    def __init__(self, map_input: TfMap):
        tfassert.is_instance(map_input, TfMap)
        super().__init__('values', map_input)
        self.element_type = map_input.element_type(deep=True)


def tfvalues(map_input: MapLike) -> TfList:
    return tflist(TfValues(cast(TfMap, typify(map_input))))
