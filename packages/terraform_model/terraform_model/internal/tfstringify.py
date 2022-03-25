# std
from types import GenericAlias
from typing import cast, Type, Union

# internal
from terraform_model.types.internal.tftype import TfType
from terraform_model.internal.tftype import is_generic
from terraform_model.mixins.expression import ExpressionMixin
from terraform_model.mixins.literal import LiteralMixin


def tfstringify(obj: Union[ExpressionMixin, TfType, Type[TfType], GenericAlias]) -> str:
    if isinstance(obj, LiteralMixin):
        return obj.literal()
    elif isinstance(obj, ExpressionMixin):
        return obj.expression()
    elif isinstance(obj, TfType):
        return str(obj)
    elif isinstance(obj, type) and issubclass(obj, TfType):
        return obj.type()
    elif is_generic(obj):
        return _stringify_generic(obj)
    else:
        raise NotImplementedError


def _stringify_generic(generic: GenericAlias) -> str:
    if len(generic.__args__) != 1:
        raise NotImplementedError
    origin = cast(Type[TfType], generic.__origin__)
    arg = cast(Type[TfType], generic.__args__[0])
    return f'{tfstringify(origin)}({tfstringify(arg)})'
