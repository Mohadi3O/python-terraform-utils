# std
from typing import cast

# internal
from terraform_model.functions.collection.internal.collection_function import TfCollectionFunction
from terraform_model.types.conversions.typify import typify
from terraform_model.types import TfSet
from terraform_model.internal.tftype import SetLike
from terraform_model.internal import tfassert


class TfSetSubtract(TfCollectionFunction):

    def __init__(self, a: TfSet, b: TfSet):
        tfassert.all_is_instance(TfSet, a, b)
        tfassert.same_type_deep(a, b)
        super().__init__('setsubtract', a, b)
        self.element_type = a.element_type()


def tfsetsubtract(a: SetLike, b: SetLike) -> TfSet:
    return TfSet(TfSetSubtract(cast(TfSet, typify(a)), cast(TfSet, typify(b))))
