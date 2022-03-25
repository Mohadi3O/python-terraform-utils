# std
from typing import cast

# internal
from terraform_model.functions.collection.internal.collection_function import TfCollectionFunction
from terraform_model.types.conversions.typify import typify
from terraform_model.types import tflist, TfList, TfMap, TfString
from terraform_model.internal.tftype import MapLike
from terraform_model.internal import tfassert


class TfKeys(TfCollectionFunction):
    element_type = TfString

    def __init__(self, map_input: TfMap):
        tfassert.is_instance(map_input, TfMap)
        super().__init__('keys', map_input)


def tfkeys(map_input: MapLike) -> TfList[TfString]:
    return tflist(TfKeys(cast(TfMap, typify(map_input))))
