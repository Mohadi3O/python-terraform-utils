# std
from __future__ import annotations
from collections import defaultdict
from contextlib import AbstractContextManager
import os
from typing import Generic, TypeVar, Optional as Opt

# internal
from terraform_model.utils.errors import TerraformModelException

# types
T = TypeVar('T')

# constants
DEFAULT_NAME = 'default'


class Scope(Generic[T], AbstractContextManager):
    _scopes: dict[str, Scope] = {}
    _stack: list[Scope] = []

    def __init__(self, name: str):
        self._name = name
        self._items: dict[str, dict[str, T]] = defaultdict(dict)
        self._parent: Opt[Scope] = None
        self._children: list[ModuleScope] = []
        self._register()

    def __enter__(self) -> Scope:
        if len(self._stack) > 0:
            self._parent = self.get_active_scope()
            self._parent.register_child(self)
        self._stack.append(self)
        return self

    def enter(self):
        self.__enter__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._stack.pop()

    @property
    def name(self):
        return self._name

    @property
    def items(self):
        return self._items

    @property
    def children(self):
        return self._children

    def _register(self):
        if self.exists(self.name):
            raise TerraformModelException(f'Scope "{self.name}" already exists')
        self._scopes[self.name] = self

    def add(self, item: T, name: str, key: str = DEFAULT_NAME):
        self.items[key][name] = item

    def get_keys(self) -> list[str]:
        return list(self.items.keys())

    def key_exists(self, key: str = DEFAULT_NAME) -> bool:
        return key in self.items

    def get_names(self, key: str = DEFAULT_NAME) -> list[str]:
        return list(self.items[key].keys())

    def item_exists(self, name: str, key: str = DEFAULT_NAME) -> bool:
        return key in self.items and name in self.items[key]

    def get_item(self, name: str, key: str = DEFAULT_NAME) -> T:
        return self.items[key][name]

    def get_items(self, key: str = DEFAULT_NAME) -> list[T]:
        return list(self.items[key].values())

    def get_dirpath(self) -> str:
        if self.name == DEFAULT_NAME:
            return '.'
        return self.name

    def register_child(self, child: Scope):
        self._children.append(child)

    def clear_scope(self):
        self._items: dict[str, dict[str, T]] = defaultdict(dict)
        self._parent: Opt[Scope] = None
        self._children: list[ModuleScope] = []

    @classmethod
    def clear_scopes(cls):
        default_scope = cls._stack[0]
        cls._scopes = {default_scope.name: default_scope}
        cls._stack = cls._stack[:1]
        default_scope.clear_scope()

    @classmethod
    def exists(cls, name: str) -> bool:
        return name in cls._scopes

    @classmethod
    def get_scope(cls, name: str = DEFAULT_NAME) -> Scope:
        return cls._scopes[name]

    @classmethod
    def get_scopes(cls) -> list[Scope]:
        return list(cls._scopes.values())

    @classmethod
    def get_active_scope(cls) -> Scope:
        return cls._stack[-1]


class ModuleScope(Scope):

    def __init__(self, name: str, module_or_function=None):
        super().__init__(name)
        self._module_or_function = module_or_function

    @property
    def module_or_function(self):
        return self._module_or_function

    def get_dirpath(self) -> str:
        if self._parent is None:
            return f'modules/{self.name}'
        else:
            return f'{self._parent.get_dirpath()}/modules/{self.name}'

    @classmethod
    def get_module_names(cls) -> list[str]:
        return [name for name, scope in cls._scopes.items() if isinstance(scope, ModuleScope)]

    @classmethod
    def get_modules(cls) -> list[ModuleScope]:
        return [scope for scope in cls._scopes.values() if isinstance(scope, ModuleScope)]
