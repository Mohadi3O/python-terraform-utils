# std
from __future__ import annotations
from inspect import Parameter, Signature
from typing import Optional as Opt, Union as U

# types
DATA_TYPE = list[U[str, list]]

# constants
MAGIC = '__magic__'
SELF = '_self_'


class Code:
    INDENT_SPACES = 4

    def __init__(self, data: Opt[DATA_TYPE] = None):
        data = [] if data is None else data
        self.data: DATA_TYPE = data

    def __add__(self, other: Code) -> Code:
        return Code(data=self.data + other.data)

    def __iadd__(self, other: Code) -> Code:
        self.data.extend(other.data)
        return self

    def append(self, *lines: str):
        for line in lines:
            self.data.append(line.strip())

    def block(self, opening_line: str) -> Code:
        self.append(opening_line)
        data = []
        self.data.append(data)
        self.append('')
        return Code(data)

    def compile(self) -> str:
        return self._compile_data(self.data, 0)

    def class_(self, name: str, *parent_classes: str) -> Class:
        parent_classes: str = '' if len(parent_classes) == 0 else f'({", ".join(parent_classes)})'
        return Class(self.block(f'class {name}{parent_classes}:').data)

    def function(self, name: str, parameters: Opt[list[dict]] = None, annotation: Opt[type] = None) -> Code:
        return self.block(f'def {name}{signature(parameters, annotation)}:')

    @classmethod
    def _compile_data(cls, data: U[str, list, DATA_TYPE], level: int = 0) -> str:
        if isinstance(data, str):
            indention = (' ' * cls.INDENT_SPACES) * level
            return f'{indention}{data}'
        if len(data) == 0:
            return cls._compile_data('pass', level)
        compiled = (
            cls._compile_data(d, level) if isinstance(d, str) else cls._compile_data(d, level + 1)
            for d in data
        )
        return '\n'.join(compiled)


class Class(Code):

    def property(self, name: str, parameters: Opt[list[dict]] = None, annotation: Opt[type] = None) -> Code:
        parameters = [] if parameters is None else parameters
        self.append('@property')
        parameters = [{'name': SELF, 'kind': Parameter.POSITIONAL_ONLY}] + parameters
        return self.function(name, parameters, annotation)

    def method(self, name: str, parameters: Opt[list[dict]] = None, annotation: Opt[type] = None) -> Code:
        parameters = [] if parameters is None else parameters
        parameters = [{'name': SELF, 'kind': Parameter.POSITIONAL_ONLY}] + parameters
        return self.function(name, parameters, annotation)


def parameter(name: str, default=MAGIC, annotation=None, kind=None) -> Parameter:
    kind = Parameter.KEYWORD_ONLY if kind is None else kind
    kwargs = {
        'name': name,
        'kind': kind,
    }
    if annotation is not None:
        kwargs['annotation'] = annotation
    if default != MAGIC:
        kwargs['default'] = default
    return Parameter(**kwargs)


def signature(parameters: Opt[list[dict]] = None, return_annotation: Opt[type] = None) -> str:
    parameters = [] if parameters is None else parameters
    kwargs = {
        'parameters': [parameter(**p) for p in parameters],
    }
    if return_annotation is not None:
        kwargs['return_annotation'] = return_annotation
    return str(Signature(**kwargs)).replace(', /', '')
