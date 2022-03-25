# std
import os

# internal
from terraform_model.version import __version__
from terraform_model.utils import log
from terraform_model.internal.tftype import TfJsonObject
from terraform_model.helpers.scope import Scope, ModuleScope, DEFAULT_NAME
from terraform_model.blocks.blocks.block import Block
from terraform_model.blocks.blocks.terraform import Terraform
from terraform_model.utils.json import dump


DIST = 'dist'
TERRAFORM_TF_JSON = 'terraform.tf.json'


def compile_terraform(scope_name: str = DEFAULT_NAME, dirpath: str = DIST):
    filepath = os.path.join(dirpath, TERRAFORM_TF_JSON)
    log.info(f'Compiling scope "{scope_name}" to path "{filepath}"')
    scope = Scope.get_scope(scope_name)
    obj = model(scope)
    dump(obj, filepath)
    for child in scope.children:
        child_dirpath = os.path.join(dirpath, 'modules', child.name)
        compile_terraform(child.name, child_dirpath)



def model(scope: Scope) -> TfJsonObject:
    model = {
        '//': {
            'terraform_model': __version__,
        },
        'terraform': Terraform.model(scope),
    }
    skip_types = Terraform.types()
    for block_type_name in scope.get_keys():
        if block_type_name not in skip_types:
            block_type = Block.get_type(block_type_name)
            model[block_type.type_name()] = block_type.model(scope)
    return model
