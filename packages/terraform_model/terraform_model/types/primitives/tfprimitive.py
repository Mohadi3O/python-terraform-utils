# std
from abc import abstractmethod

# internal
from ..internal.tftype import TfType
from terraform_model.utils.types import is_json_primitive
from terraform_model.mixins import HashableMixin


class TfPrimitive(TfType, HashableMixin):

    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError

    def __hash__(self):
        return hash(self.data)

    def expression(self) -> str:
        if is_json_primitive(self.data):
            return str(self)
        else:
            return super().expression()
