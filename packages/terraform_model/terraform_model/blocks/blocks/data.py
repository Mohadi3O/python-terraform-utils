# std
from typing import Optional as Opt, Type, Union

# internal
from ...internal.tftype import TfJsonLike
from terraform_model.types.internal.tftype import TfType
from terraform_model.types.conversions.typify import typify
from .block import Block


class Data(Block):

    def __init__(self, sub_type: str, name: str, **kwargs: TfJsonLike):
        super().__init__(sub_type, name, **kwargs)

    def __str__(self):
        return f'data.{self.sub_type}.{self.name}'

    @classmethod
    def type(cls):
        return Data

    @classmethod
    def type_name(cls):
        return 'data'

    @classmethod
    def new(cls, sub_type: str, name: str, **kwargs: TfJsonLike) -> TfType:
        return typify(Data(sub_type, name, **kwargs))


def data(sub_type: str, name: str, **kwargs: TfJsonLike):
    return Data.new(sub_type, name, **kwargs)
