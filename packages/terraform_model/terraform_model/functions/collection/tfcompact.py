# internal
from terraform_model.functions.collection.internal.collection_function import TfCollectionFunction
from terraform_model.types import TfList, TfString, tflist
from terraform_model.internal.tftype import ListLike
from terraform_model.internal import tfassert


class TfCompact(TfCollectionFunction):

    def __init__(self, list_input: TfList[TfString]):
        tfassert.all_is_instance(TfList[TfString], list_input)
        super().__init__('compact', list_input)
        self.element_type = TfString


def tfcompact(list_input: ListLike) -> TfList[TfString]:
    return tflist(TfCompact(list_input))
