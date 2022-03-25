# std
from typing import cast, Union

# internal
from terraform_model.functions.collection.internal.collection_function import TfCollectionFunction
from terraform_model.types.conversions.typify import typify
from terraform_model.types import TfList, TfSet
from terraform_model.internal import tfassert
from terraform_model.internal.tftype import tftype, ListLike, SetLike


class TfSetProduct(TfCollectionFunction):

    def __init__(self, *sets_or_lists: Union[TfList, TfSet]):
        tfassert.all_is_instance((TfList, TfSet), *sets_or_lists)
        tfassert.same_type(*sets_or_lists)
        tfassert.same_element_type(*sets_or_lists)
        super().__init__('setproduct', *sets_or_lists)
        self.element_type = sets_or_lists[0].element_type()


def tfsetproduct(*sets_or_lists: Union[ListLike, SetLike]) -> Union[TfList, TfSet]:
    sets_or_lists = list(map(typify, sets_or_lists))
    return cast(Union[TfList, TfSet], tftype(sets_or_lists[0])(TfSetProduct(*sets_or_lists)))
