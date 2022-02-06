# std
from __future__ import annotations
from inspect import Parameter
from typing import Optional as Opt, Type, Union

# internal
from terraform_model.utils.types import JsonObject
from terraform_model.helpers.scope import Scope
from terraform_model.blocks.blocks.block import Block
from terraform_model.mixins import CompareMixin, MathMixin
from terraform_model.types.terraform_type import TerraformType
from terraform_model.types.unknown import Unknown
from terraform_model.types.typify import typify


class Variable(Block, CompareMixin, MathMixin):

    def __init__(
            self,
            name: str,
            default: Opt[any] = None,
            var_type: Opt[Union[str, Type[TerraformType]]] = None,
            **kwargs,
    ):
        if default is not None:
            kwargs['default'] = default
        if var_type is not None:
            if not isinstance(var_type, str) and issubclass(var_type, TerraformType):
                var_type = var_type.type()
            kwargs['type'] = var_type
        super().__init__(None, name, **kwargs)

    def __str__(self):
        return f'var.{self.name}'

    @classmethod
    def type(cls):
        return Variable

    @classmethod
    def type_name(cls):
        return 'variable'

    @classmethod
    def model(cls, scope: Scope[Block]) -> JsonObject:
        blocks = scope.get_items(cls.type_name())
        model = {}
        for block in blocks:
            model[block.name] = block.json()
        return model

    @classmethod
    def new(
            cls,
            name: str,
            default: Opt[any] = None,
            type: Opt[Union[str, Type[TerraformType]]] = None,
            **kwargs,
    ) -> TerraformType:
        var = Variable(name, default=default, var_type=type, **kwargs)
        return typify(var)

    @classmethod
    def from_parameter(cls, parameter: Parameter) -> TerraformType:
        name = parameter.name
        default = None if parameter.default is Parameter.empty else parameter.default
        _type = None if parameter.annotation is Parameter.empty else parameter.annotation
        return cls.new(name, default=default, type=_type)



def variable(
        name: str,
        default: Opt[any] = None,
        type: Opt[Union[str, Type[TerraformType]]] = None,
        **kwargs,
):
    return Variable.new(name, default=default, type=type, **kwargs)
