# internal
from .provider import Provider


def load_provider_schemas(provider_schemas) -> list[Provider]:
    providers = []
    for name, provider_schema in provider_schemas.get('provider_schemas', {}).items():
        providers.append(Provider(name, provider_schema))
    return providers
