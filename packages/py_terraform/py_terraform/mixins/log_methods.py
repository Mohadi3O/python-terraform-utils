# internal
from ..utils.logger import log


def decorator(func):
    def wrapper(self, *args, **kwargs):
        log.silly(f'{self.__class__.__name__}.{func.__name__} {args} {kwargs}')
        return func(self, *args, **kwargs)
    return wrapper


class LogMethodsMixin:

    def __new__(cls, *args, **kwargs):
        c = super().__new__(cls)
        for key, val in cls.__dict__.items():
            if callable(val):
                setattr(cls, key, decorator(getattr(cls, key)))
        return c
