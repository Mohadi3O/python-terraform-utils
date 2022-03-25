# std
from __future__ import annotations
from typing import Optional as Opt

# internal
from terraform_model.types.structurals.tfstructural import TfStructural
from terraform_model.utils.json import dumps
from terraform_model.mixins.literal import LiteralMixin


class TfObject(TfStructural):

    def __init__(self, _data: Opt = None, **kwargs):
        data = kwargs if _data is None else _data
        super().__init__(data)

    def __str__(self) -> str:
        if isinstance(self.data, dict):
            return dumps(self.data)
        else:
            return str(self.data)

    @classmethod
    def new(cls, _data: Opt = None, **kwargs) -> TfObject:
        if _data is not None:
            return cls(_data)
        elif len(kwargs) == 0:
            return _empty
        else:
            return cls(**kwargs)


class TfObjectLiteral(TfObject, LiteralMixin):

    def __init__(self, data: dict):
        super().__init__(data)


def tfobject(_data: Opt = None, **kwargs) -> TfObject:
    return TfObject.new(_data, **kwargs)


_empty = TfObject()
