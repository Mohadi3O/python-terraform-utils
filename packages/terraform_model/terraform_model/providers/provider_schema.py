# std

# internal
from ..utils.types import JsonObject
from .schema import SchemaABC
from .resource_schema import ResourceSchema
from .data_source_schema import DataSourceSchema


class ProviderSchema(SchemaABC):

    def __init__(self, name: str, schema: JsonObject):
        super().__init__(name, schema)
        self._load_resource_schemas()
        self._load_data_source_schemas()

    def _load_resource_schemas(self):
        for name, schema in self.schema.get('resource_schemas', {}).items():
            ResourceSchema(name, schema)

    def _load_data_source_schemas(self):
        for name, schema in self.schema.get('data_source_schemas', {}).items():
            DataSourceSchema(name, schema)
