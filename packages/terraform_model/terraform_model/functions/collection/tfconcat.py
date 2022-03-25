# internal
from terraform_model.functions.collection.internal.collection_function import TfCollectionFunction
from terraform_model.types import tflist, TfList
from terraform_model.internal.tftype import ListLike
from terraform_model.internal import tfassert


class TfConcat(TfCollectionFunction):

    def __init__(self, list0: ListLike, list1: ListLike, *list_inputs: ListLike):
        tfassert.all_is_instance(TfList, list0, list1, *list_inputs)
        tfassert.same_type_deep(list0, list1, *list_inputs)
        super().__init__('concat', list0, list1, *list_inputs)
        self.element_type = list0.element_type(deep=True)


def tfconcat(list0: ListLike, list1: ListLike, *list_inputs: ListLike) -> TfList:
    return tflist(TfConcat(list0, list1, *list_inputs))
