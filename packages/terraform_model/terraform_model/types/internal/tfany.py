# std
from __future__ import annotations
from typing import Optional as Opt

# internal
from terraform_model.types.internal.tftype import TfType
from terraform_model.mixins import *


class TfAny(TfType, CompareMixin, GetAttrMixin, GetItemMixin, MathMixin, LogicalMixin):

    def __str__(self):
        return str(self.data)

    @classmethod
    def new(cls, data: Opt = None) -> TfAny:
        return TfAny(data)


def tfany(data: Opt = None) -> TfAny:
    return TfAny.new(data)
