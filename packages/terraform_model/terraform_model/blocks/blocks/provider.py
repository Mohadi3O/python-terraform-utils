# std
from __future__ import annotations
from typing import Optional as Opt

# internal
from ...internal.tftype import TfJsonLike, TfJsonObject
from terraform_model.helpers.scope import Scope
from .block import Block


class Provider(Block):

    def __init__(self, sub_type: str, alias: Opt[str] = None, **kwargs: TfJsonLike):
        if alias:
            kwargs['alias'] = alias
        super().__init__(sub_type, None, **kwargs)

    @property
    def name(self):
        if 'alias' in self.data:
            return f'{self.sub_type}.{self.data["alias"]}'
        return self.sub_type

    @classmethod
    def type(cls):
        return Provider

    @classmethod
    def type_name(cls):
        return 'provider'

    @classmethod
    def model(cls, scope: Scope[Block]) -> TfJsonObject:
        blocks = scope.get_items(cls.type_name())
        model = {}
        for block in blocks:
            if block.sub_type not in model:
                model[block.sub_type] = []
            model[block.sub_type].append(block.json())
        return model
