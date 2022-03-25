# std
from contextlib import AbstractContextManager

# internal
from terraform_model import conf


class StrictTyping(AbstractContextManager):

    def __init__(self, strict_typing: bool = True):
        self._strict_typing = strict_typing
        self._previous_value = conf.strict_typing

    def __enter__(self):
        conf.strict_typing = self._strict_typing

    def __exit__(self, exc_type, exc_val, exc_tb):
        conf.strict_typing = self._previous_value
