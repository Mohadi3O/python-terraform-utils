# std
from contextlib import AbstractContextManager
import os
from pathlib import Path
from typing import TextIO


class Open(AbstractContextManager):

    def __init__(self, filepath: str, **kwargs):
        self._filepath = filepath
        self._kwargs = kwargs
        self._fh = None

    def __enter__(self) -> TextIO:
        Path(os.path.dirname(self._filepath)).mkdir(parents=True, exist_ok=True)
        self._fh = open(self._filepath, **self._kwargs)
        return self._fh

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._fh.close()
