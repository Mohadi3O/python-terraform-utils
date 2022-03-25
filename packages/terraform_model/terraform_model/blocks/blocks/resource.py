# std
from __future__ import annotations

# internal
from .block import Block
from ...internal.tftype import TfJsonLike
from terraform_model.types.primitives.tfstring import TfString


class Resource(Block):

    def __init__(self, sub_type: str, name: str, **kwargs: TfJsonLike):
        super().__init__(sub_type, name, **kwargs)

    def __rshift__(self, other: Resource):
        self.depends_on(other)

    def depends_on(self, other: Resource):
        if 'depends_on' not in self.data:
            self.data['depends_on'] = []
        self.data['depends_on'].append(str(other))

    @classmethod
    def type(cls):
        return Resource

    @classmethod
    def type_name(cls):
        return 'resource'
