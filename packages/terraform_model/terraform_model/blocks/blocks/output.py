# std
from __future__ import annotations

# internal
from terraform_model.helpers.types import TfJson, TfJsonObject
from terraform_model.helpers.scope import Scope
from .block import Block


class Output(Block):

    def __init__(self, name: str, value):
        super().__init__(None, name, value=value)

    @classmethod
    def type(cls):
        return Output

    @classmethod
    def type_name(cls):
        return 'output'

    @classmethod
    def model(cls, scope: Scope[Block]) -> TfJsonObject:
        blocks = scope.get_items(cls.type_name())
        model = {}
        for block in blocks:
            model[block.name] = block.json()
        return model
