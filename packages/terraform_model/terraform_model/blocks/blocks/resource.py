# std
from __future__ import annotations

# internal
from .block import Block
from terraform_model.helpers.types import TfJson


class Resource(Block):

    def __init__(self, sub_type: str, name: str, **kwargs: TfJson):
        super().__init__(sub_type, name, **kwargs)

    def __rshift__(self, other: Resource):
        if 'depends_on' not in self.data:
            self.data['depends_on'] = []
        self.data['depends_on'].append(str(other))

    @classmethod
    def type(cls):
        return Resource

    @classmethod
    def type_name(cls):
        return 'resource'
