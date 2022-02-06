# external
from py_terraform import Terraform

# internal
from .provider import Provider


def load_provider_schemas(**tf_kwargs):
    tf = Terraform(**tf_kwargs)
    provider_schemas = tf.providers_schema(json=True, capture=True)
    for name, provider_schema in provider_schemas.get('provider_schemas', {}).items():
        Provider(name, provider_schema)
