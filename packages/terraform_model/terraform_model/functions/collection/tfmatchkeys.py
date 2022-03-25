# internal
from terraform_model.functions.collection.internal.collection_function import TfCollectionFunction
from terraform_model.types.conversions.typify import typify
from terraform_model.types import tflist, TfList
from terraform_model.internal import tfassert
from terraform_model.internal.tftype import ListLike


class TfMatchKeys(TfCollectionFunction):

    def __init__(self, valueslist: TfList, keyslist: TfList, searchset: TfList):
        tfassert.is_instance(valueslist, TfList)
        tfassert.is_instance(keyslist, TfList)
        tfassert.is_instance(searchset, TfList)
        tfassert.same_type_deep(keyslist, searchset)
        super().__init__('matchkeys', valueslist, keyslist, searchset)
        self.element_type = valueslist.element_type(deep=True)


def tfmatchkeys(valueslist: ListLike, keyslist: ListLike, searchset: ListLike) -> TfList:
    valueslist = typify(valueslist).to_list()
    keyslist = typify(keyslist).to_list()
    searchset = typify(searchset).to_list()
    return tflist(TfMatchKeys(valueslist, keyslist, searchset))
