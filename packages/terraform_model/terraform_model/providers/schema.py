# std
from __future__ import annotations
from abc import ABC
from collections import defaultdict

# internal
from ..utils.types import JsonObject


class SchemaABC(ABC):
    _schemas: dict[str, list[SchemaABC]] = defaultdict(list)

    def __init__(self, name: str, schema: JsonObject):
        self._name = name
        self._schema = schema
        self._schemas[self.__class__.__name__].append(self)

    @property
    def name(self):
        return self._name

    @property
    def schema(self):
        return self._schema
