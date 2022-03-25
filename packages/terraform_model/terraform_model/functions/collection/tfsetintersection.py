# internal
from terraform_model.functions.collection.internal.collection_function import TfCollectionFunction
from terraform_model.types.conversions.typify import typify
from terraform_model.types import tfset, TfSet
from terraform_model.internal.tftype import SetLike
from terraform_model.internal import tfassert


class TfSetIntersection(TfCollectionFunction):

    def __init__(self, *sets: TfSet):
        tfassert.all_is_instance(TfSet, *sets)
        tfassert.same_type_deep(*sets)
        super().__init__('setintersection', *sets)
        self.element_type = sets[0].element_type(deep=True)


def tfsetintersection(*sets: SetLike) -> TfSet:
    return tfset(TfSetIntersection(*map(typify, sets)))
