# std
from abc import abstractmethod

# internal
from terraform_model.utils.errors import TerraformTypeError


class HashableMixin:

    @abstractmethod
    def __hash__(self):
        raise NotImplementedError


class NonHashableMixin:

    def __hash__(self):
        raise TerraformTypeError(f'Type {type(self)} is not hashable.')
