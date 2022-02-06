from abc import abstractmethod

from terraform_model.types.terraform_type import TerraformType
from terraform_model.utils.types import is_json_atomic


class Atomic(TerraformType):

    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError

    def expression(self) -> str:
        if is_json_atomic(self.data):
            return str(self)
        else:
            return super().expression()
