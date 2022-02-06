# internal
from terraform_model.utils.errors import TerraformTypeError
from terraform_model.types.terraform_type import TerraformType
from terraform_model.types.atomics import *
from terraform_model.types.atomics.bool import Bool
from terraform_model.types.atomics.null import Null
from terraform_model.types.collections import *


def same_type(this: TerraformType, that: TerraformType):
    if not (
            # both Bool
            (isinstance(this, Bool) and isinstance(that, Bool))
            # both Null
            or (isinstance(this, Null) and isinstance(that, Null))
            # both Number
            or (isinstance(this, Number) and isinstance(that, Number))
            # both String
            or (isinstance(this, String) and isinstance(that, String))
            # both List
            or (isinstance(this, List) and isinstance(that, List))
            # both Map
            or (isinstance(this, Map) and isinstance(that, Map))
    ):
        raise TerraformTypeError(f'{repr(this)} and {repr(that)} are not the same type')


def is_number(something: TerraformType):
    if not isinstance(something, Number):
        raise TerraformTypeError(f'Expected a number. Got {repr(something)}')
