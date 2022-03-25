# std
from typing import cast

# internal
from terraform_model.functions.collection.internal.collection_function import TfCollectionFunction
from terraform_model.types.conversions.typify import typify
from terraform_model.types import tfmap, TfList, TfMap, TfString
from terraform_model.internal.tftype import ListLike
from terraform_model.internal import tfassert


class TfZipMap(TfCollectionFunction):

    def __init__(self, keyslist: TfList[TfString], valueslist: TfList):
        tfassert.is_instance(keyslist, TfList[TfString])
        tfassert.is_instance(valueslist, TfList)
        super().__init__('zipmap', keyslist, valueslist)
        self.element_type = valueslist.element_type(deep=True)


def tfzipmap(keyslist: ListLike, valueslist: ListLike) -> TfMap:
    return tfmap(TfZipMap(cast(TfList, typify(keyslist)), cast(TfList, typify(valueslist))))
