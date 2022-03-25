# std
import os
import shutil

# internal
from terraform_model.utils import log
from terraform_model.providers.load import load_provider_schemas
from terraform_model.providers.generate import generate_providers
from terraform_model.cli.subcommands.terraform import default_terraform


def get_providers(args):
    if os.path.isdir('./providers'):
        shutil.rmtree('./providers')
    log.info('Generating Terraform providers')
    provider_schemas = _get_provider_schemas()
    providers = load_provider_schemas(provider_schemas)
    generate_providers(providers)


def _get_provider_schemas():
    tf = default_terraform()
    return tf.providers_schema(json=True, capture=True)
