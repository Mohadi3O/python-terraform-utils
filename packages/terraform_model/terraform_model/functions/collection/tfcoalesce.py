# internal
from terraform_model.functions.collection.internal.collection_function import TfCollectionFunction
from terraform_model.types.conversions.typify import typify
from terraform_model.types.internal import TfType
from terraform_model.internal import tfassert
from terraform_model.internal.tftype import tftype, AnyLike


class TfCoalesce(TfCollectionFunction):

    def __init__(self, *args: TfType):
        tfassert.same_type(*args)
        super().__init__('coalesce', *args)


def tfcoalesce(*args: AnyLike) -> TfType:
    _args = [typify(a) for a in args]
    tftype_0 = tftype(_args[0])
    return tftype_0.new(TfCoalesce(*_args))
