# internal
from terraform_model.functions.collection.internal.collection_function import TfCollectionFunction
from terraform_model.types.conversions.typify import typify
from terraform_model.types import TfList, tflist
from terraform_model.internal.tftype import ListLike
from terraform_model.internal import tfassert


class TfCoalesceList(TfCollectionFunction):

    def __init__(self, *args: TfList):
        tfassert.all_is_instance(TfList, *args)
        tfassert.same_type_deep(*args)
        super().__init__('coalescelist', *args)
        self.element_type = args[0].element_type(deep=True)


def tfcoalescelist(*args: ListLike) -> TfList:
    _args = [typify(a) for a in args]
    return tflist(TfCoalesceList(*_args))
