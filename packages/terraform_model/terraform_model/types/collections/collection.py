from abc import abstractmethod

from terraform_model.types.terraform_type import TerraformType


class Collection(TerraformType):

    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError
