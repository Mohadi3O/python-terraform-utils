# internal
from terraform_model.functions.string._string import StringTfFunction
from terraform_model.types import TfString
from terraform_model.internal.tftype import StringLike, AnyLike


class TfFormat(StringTfFunction):

    def __init__(self, spec: StringLike, *values: AnyLike):
        super().__init__('format', spec, *values)


def tfformat(spec: StringLike, *values: AnyLike) -> TfString:
    return TfString(TfFormat(spec, *values))
