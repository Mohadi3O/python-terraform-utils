# std
from __future__ import annotations
from abc import ABC
from typing import Optional as Opt, Type

# internal
from terraform_model.mixins import ExpressionMixin, GetAttrMixin
from terraform_model.helpers.types import TfJsonObject
from terraform_model.helpers.scope import Scope, DEFAULT_NAME
from terraform_model.types.typify import typify


class Block(ABC, ExpressionMixin, GetAttrMixin):
    _types: dict[str, Type[Block]] = {}

    def __init__(
            self,
            sub_type: Opt[str],
            name: Opt[str],
            **data,
    ):
        self._sub_type: Opt[str] = sub_type
        self._name: Opt[str] = name
        self._data: dict = {k: typify(v) for k, v in data.items()}
        type_name = self.type_name()
        if type_name not in self._types:
            self._types[type_name] = self.type()
        self._scope: Scope = self._register()

    def __str__(self):
        return f'{self.sub_type}.{self.name}'

    @property
    def data(self):
        return self._data

    @classmethod
    def type_name(cls):
        raise NotImplementedError

    @classmethod
    def type(cls):
        raise NotImplementedError

    @property
    def sub_type(self):
        return self._sub_type

    @property
    def name(self):
        return self._name

    @property
    def scope(self):
        return self._scope

    def json(self) -> TfJsonObject:
        return self._data

    def _register(self):
        scope = Scope.get_active_scope()
        scope.add(self, name=self.name, key=self.type_name())
        return scope

    @classmethod
    def exists(cls, name: str) -> bool:
        scope = Scope.get_active_scope()
        return scope.item_exists(name=name, key=cls.type_name())

    @classmethod
    def get_type(cls, type_name: str) -> Type[Block]:
        return cls._types[type_name]

    @classmethod
    def model(cls, scope: Scope[Block]) -> TfJsonObject:
        blocks = scope.get_items(cls.type_name())
        model = {}
        for block in blocks:
            if block.sub_type not in model:
                model[block.sub_type] = {}
            model[block.sub_type][block.name] = block.json()
        return model


Scope[Block](DEFAULT_NAME).enter()
