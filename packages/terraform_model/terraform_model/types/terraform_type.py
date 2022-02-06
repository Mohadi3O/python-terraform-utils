from abc import abstractmethod

from terraform_model.mixins import ExpressionMixin, ToMixin


class TerraformType(ExpressionMixin, ToMixin):

    def __init__(self, data):
        if isinstance(data, self.__class__):
            data = data.data
        self._data = data

    @property
    def data(self):
        return self._data

    def __repr__(self):
        return f'<{self.type()}> {str(self)}'

    @abstractmethod
    def __str__(self):
        raise NotImplementedError

    @classmethod
    def type(cls) -> str:
        return cls.__name__.lower().replace('literal', '')

    @classmethod
    def new(cls, *args, **kwargs):
        return cls(*args, **kwargs)
