# std
from abc import abstractmethod
from typing import Optional as Opt

# internal
from terraform_model.mixins import ExpressionMixin, ToMixin


class TfType(ExpressionMixin, ToMixin):

    def __init__(self, data):
        if isinstance(data, self.__class__):
            data = data.data
        self._data = data

    @property
    def data(self):
        return self._data

    def __repr__(self):
        return f'<{self.type().replace("tf", "")}> {str(self)}'

    @abstractmethod
    def __str__(self):
        raise NotImplementedError

    @classmethod
    def type(cls) -> str:
        return cls.__name__.lower().replace('tf', '').replace('literal', '')

    @classmethod
    @abstractmethod
    def new(cls, data: Opt = None):
        raise NotImplementedError

    @classmethod
    def empty(cls):
        return cls.new()
