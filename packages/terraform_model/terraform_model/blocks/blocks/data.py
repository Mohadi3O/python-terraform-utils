# std

# internal
from terraform_model.helpers.types import TfJson
from .block import Block


class Data(Block):

    def __init__(self, sub_type: str, name: str, **kwargs: TfJson):
        super().__init__(sub_type, name, **kwargs)

    def __str__(self):
        return f'data.{self.sub_type}.{self.name}'

    @classmethod
    def type(cls):
        return Data

    @classmethod
    def type_name(cls):
        return 'data'
