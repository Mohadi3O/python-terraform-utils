# std
from __future__ import annotations
from typing import Optional as Opt

# internal
from terraform_model import conf
from terraform_model.types.internal.tftype import TfType
from terraform_model.types.internal.tfany import TfAny


class TfUnknown(TfType):

    def __str__(self):
        return str(self.data)

    @classmethod
    def type(cls) -> str:
        return 'unknown'

    @classmethod
    def new(cls, data: Opt = None) -> TfUnknown:
        if conf.strict_typing:
            return TfUnknownStrict(data)
        else:
            return TfUnknownLoose(data)


class TfUnknownStrict(TfUnknown):
    pass


class TfUnknownLoose(TfUnknown, TfAny):
    pass


def tfunknown(data: Opt = None) -> TfUnknown:
    return TfUnknown.new(data)
