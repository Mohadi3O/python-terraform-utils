# internal
from ..utils.types import JsonObject
from .provider_schema import ProviderSchema


class Provider:
    _providers = []

    def __init__(self, name: str, schema: JsonObject):
        self._name = name
        self._schema = ProviderSchema(name, schema)
        self._providers.append(self)
