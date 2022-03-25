# std
from typing import cast

# internal
from terraform_model.functions.collection.internal.collection_function import TfCollectionFunction
from terraform_model.types.conversions.typify import typify
from terraform_model.types import tfmap, TfMap
from terraform_model.internal.tftype import MapLike
from terraform_model.internal import tfassert


class TfMerge(TfCollectionFunction):

    def __init__(self, *map_inputs: TfMap):
        tfassert.all_is_instance(TfMap, *map_inputs)
        tfassert.same_type_deep(*map_inputs)
        super().__init__('merge', *map_inputs)
        self.element_type = map_inputs[0].element_type(deep=True)


def tfmerge(*map_inputs: MapLike) -> TfMap:
    map_inputs = [cast(TfMap, typify(m)) for m in map_inputs]
    return tfmap(TfMerge(*map_inputs))
