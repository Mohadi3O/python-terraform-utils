# std
from abc import abstractmethod

# internal
from terraform_model.types.internal.tftype import TfType


class TfStructural(TfType):

    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError
