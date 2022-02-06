# std
from hashlib import sha1
from inspect import signature
from functools import partial
from typing import Optional as Opt

# internal
from terraform_model.helpers.types import TfJson
from terraform_model.types.typify import to
from terraform_model.blocks.blocks.variable import Variable
from terraform_model.blocks.blocks.output import Output
from terraform_model.blocks.blocks.module import NestedModule
from terraform_model.helpers.scope import Scope, ModuleScope


def module(func):
    nested_module_name = func.__name__
    with ModuleScope(nested_module_name, func):
        parameters = signature(func).parameters
        variables = [Variable.from_parameter(parameter) for parameter in parameters.values()]
        func(*variables)
    nested_module_scope = Scope.get_scope(nested_module_name)
    nested_module_scope_dirpath = nested_module_scope.get_dirpath()
    PartialNestedModule = partial(NestedModule, nested_module_scope_dirpath)
    return PartialNestedModule


def _name_generator(name: str):
    used = []

    def generator(hashable) -> str:
        if not used:
            used.append(True)
            return name
        return f'{name}_{sha1(str(hashable).encode("utf-8")).hexdigest()[:8]}'

    return generator


def module_function(func):
    nested_module_name = func.__name__
    with ModuleScope(nested_module_name, func):
        parameters = signature(func).parameters
        variables = [Variable.from_parameter(parameter) for parameter in parameters.values()]
        _output = func(*variables)
        if not isinstance(_output, Output):
            _output = Output('return', _output)
    nested_module_scope = Scope.get_scope(nested_module_name)
    nested_module_scope_dirpath = nested_module_scope.get_dirpath()
    PartialNestedModule = partial(NestedModule, nested_module_scope_dirpath)
    generate_name = _name_generator(nested_module_name)

    def wrapper(name: Opt[str] = None, **kwargs: TfJson):
        if name is None:
            name = generate_name(kwargs)
        instance_output = getattr(PartialNestedModule(name, **kwargs), _output.name)
        return to(instance_output, _output.data['value'])

    return wrapper
