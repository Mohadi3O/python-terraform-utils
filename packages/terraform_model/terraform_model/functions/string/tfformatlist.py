# internal
from terraform_model.functions.string._string import StringTfFunction
from terraform_model.types import TfList, TfString
from terraform_model.internal.tftype import StringLike, AnyLike


class TfFormatList(StringTfFunction):

    def __init__(self, spec: StringLike, *values: AnyLike):
        super().__init__('formatlist', spec, *values)


def tfformatlist(spec: StringLike, *values: AnyLike) -> TfList[TfString]:
    return TfList(TfFormatList(spec, *values))
