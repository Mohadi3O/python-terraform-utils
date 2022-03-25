# std
from typing import cast

# internal
from terraform_model.functions.collection.internal.collection_function import TfCollectionFunction
from terraform_model.types.conversions.typify import typify
from terraform_model.types import TfMap, TfString, TfCollection
from terraform_model.types.internal import TfType
from terraform_model.internal.tftype import StringLike, MapLike, AnyLike
from terraform_model.internal import tfassert


class TfLookup(TfCollectionFunction):

    def __init__(self, map_input: TfMap, key: TfString, default: TfType):
        tfassert.is_instance(map_input, TfMap)
        tfassert.is_instance(key, TfString)
        tfassert.is_instance(default, TfType)
        tfassert.is_instance(default, map_input.element_type(deep=True))
        super().__init__('lookup', map_input, key, default)
        if isinstance(default, TfCollection):
            self.element_type = default.element_type(deep=True)


def tflookup(map_input: MapLike, key: StringLike, default: AnyLike) -> TfType:
    map_input = cast(TfMap, typify(map_input))
    element_type = map_input.element_type()
    key = cast(TfString, typify(key))
    default = typify(default)
    return element_type.new(TfLookup(map_input, key, default))
