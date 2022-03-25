# std
from __future__ import annotations

# internal
from ..utils.types import JsonObject
from .provider_schema import ProviderSchema


class Provider:
    providers = {}

    def __init__(self, name: str, schema: JsonObject):
        print(name)
        self.name = name
        self.schema = ProviderSchema(name, schema)
        self.providers[name] = self

    @classmethod
    def get_provider(cls, name: str) -> Provider:
        return cls.providers[name]
