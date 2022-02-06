# std
from abc import ABC
from collections import namedtuple
from itertools import chain
from typing import Optional, TypeVar, Union

T = TypeVar('T')
ArgStr = str
ArgTuple1 = tuple[str]
ArgTuple2 = tuple[str, str]
ArgTuple3 = tuple[str, str, str]
ArgTuple = Union[ArgTuple1, ArgTuple2, ArgTuple3]
ArgType = Union[ArgStr, ArgTuple]
KeyVal = namedtuple('KeyVal', ['key', 'val'])


class ArgABC(ABC):

    def __init__(self, name: Optional[str], value: T):
        self._name: Optional[str] = name
        self._value: T = value

    def __str__(self):
        if self._value is None:
            return ''
        elif self._name is None:
            return self.value
        return f'{self.name}={self.value}'

    def __repr__(self):
        return self.__str__()

    @property
    def name(self):
        return f'-{self._name.replace("_", "-")}'

    @property
    def value(self):
        return self._value


class BoolArg(ArgABC):

    @property
    def value(self):
        return str(self._value).lower()


class FlagArg(BoolArg):

    def __str__(self):
        return self.name if self._value else ''


class StringArg(ArgABC):
    pass


class KeyValArg(ArgABC):

    def __init__(self, name: str, value: tuple[str, str]):
        super().__init__(name, f'"{value[0]}={value[1]}"')


class PositionalArg(ArgABC):

    def __init__(self, _: None, value: T):
        super().__init__(None, value)


ARGS = {
    'auto_approve': FlagArg,
    'backend': BoolArg,
    'backend_config': StringArg,
    'chdir': StringArg,
    'compact_warnings': FlagArg,
    'config': StringArg,
    'destroy': FlagArg,
    'detail_exitcode': FlagArg,
    'force_copy': FlagArg,
    'from_module': StringArg,
    'get': BoolArg,
    'get_plugins': BoolArg,
    'help': FlagArg,
    'ignore_remote_version': BoolArg,
    'input': BoolArg,
    'install_autocomplete': FlagArg,
    'json': FlagArg,
    'lock': BoolArg,
    'lock_timeout': StringArg,
    'lockfile': StringArg,
    'migrate_state': FlagArg,
    'no_color': FlagArg,
    'out': StringArg,
    'parallelism': StringArg,
    'plugin_dir': StringArg,
    'raw': FlagArg,
    'reconfigure': FlagArg,
    'refresh': BoolArg,
    'refresh_only': FlagArg,
    'replace': StringArg,
    'state': StringArg,
    'test': KeyValArg,
    'target': StringArg,
    'uninstall_autocomplete': FlagArg,
    'upgrade': FlagArg,
    'var': KeyValArg,
    'var_file': StringArg,
}


def fmt_arg(name: str, value: T) -> str:
    return str(ARGS.get(name, StringArg)(name, value))


def fmt_key_val_arg(name: str, key: str, val: str) -> str:
    return str(KeyValArg(name, (key, val)))


def fmt_positional(value: str) -> str:
    return str(PositionalArg(None, value))


def fmt_args(*args: ArgType, **kwargs) -> list[str]:
    args_str = [a for a in args if isinstance(a, str)]
    args_tuple1 = [a[0] for a in args if isinstance(a, tuple) and len(a) == 1]
    args_tuple2 = [a for a in args if isinstance(a, tuple) and len(a) == 2]
    args_tuple3 = [a for a in args if isinstance(a, tuple) and len(a) == 3]
    positionals = [fmt_positional(p) for p in chain(args_str, args_tuple1)]
    kwargs = [fmt_arg(*x) for x in chain(args_tuple2, kwargs.items())]
    keyvals = [fmt_key_val_arg(*x) for x in args_tuple3]
    all_args = kwargs + keyvals + positionals
    filtered_args = [x for x in all_args if x != '']
    return filtered_args
