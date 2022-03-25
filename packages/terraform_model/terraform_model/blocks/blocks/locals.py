# internal
from ...internal.tftype import TfJsonObject
from terraform_model.helpers.scope import Scope
from .block import Block
from terraform_model.types.internal.tftype import TfType
from terraform_model.types.conversions.typify import typify


class Local(Block):

    def __init__(self, name: str, value):
        super().__init__(None, name)
        self._value: TfType = typify(value)

    def __str__(self):
        return f'local.{self.name}'

    @property
    def value(self):
        return self._value

    @classmethod
    def type_name(cls):
        return 'locals'

    @classmethod
    def type(cls):
        return Local

    @classmethod
    def model(cls, scope: Scope[Block]) -> TfJsonObject:
        blocks = scope.get_items(cls.type_name())
        _model = {}
        for block in blocks:
            _model[block.name] = block.value
        return _model

    @classmethod
    def new(cls, name: str, value) -> TfType:
        return typify(Local(name, value))


def local(name: str, value):
    return Local.new(name, value)
