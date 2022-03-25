# std

# internal
from ..utils.types import JsonObject
from .schema import SchemaABC
from .resource_schema import ResourceSchema
from .data_source_schema import DataSourceSchema


class ProviderSchema(SchemaABC):

    def __init__(self, name: str, schema: JsonObject):
        super().__init__(name, schema)
        self.resources = self._load_resource_schemas()
        self.data_sources = self._load_data_source_schemas()

    def _load_resource_schemas(self):
        resources = []
        for name, schema in self.schema.get('resource_schemas', {}).items():
            resources.append(ResourceSchema(name, schema))
        return resources

    def _load_data_source_schemas(self):
        data_sources = []
        for name, schema in self.schema.get('data_source_schemas', {}).items():
            data_sources.append(DataSourceSchema(name, schema))
        return data_sources
