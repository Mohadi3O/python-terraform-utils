# std

# internal
from terraform_model.functions.collection.internal.collection_function import TfCollectionFunction
from terraform_model.types.conversions.typify import typify
from terraform_model.types import TfSet
from terraform_model.internal.tftype import SetLike
from terraform_model.internal import tfassert


class TfSetUnion(TfCollectionFunction):

    def __init__(self, *sets: TfSet):
        tfassert.all_is_instance(TfSet, *sets)
        tfassert.same_type_deep(*sets)
        super().__init__('setunion', *sets)
        self.element_type = sets[0].element_type()


def tfsetunion(*sets: SetLike) -> TfSet:
    return TfSet(TfSetUnion(*map(typify, sets)))
