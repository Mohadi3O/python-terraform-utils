# std
from __future__ import annotations
from typing import Dict, List, Union

# internal
from terraform_model.types import String, Number, List as _List, Map
from terraform_model.types.atomics.bool import Bool
from terraform_model.types.atomics.null import Null


BoolLike = Union[bool, Bool]
NullLike = Union[None, Null]
StringLike = Union[str, String]
NumberLike = Union[int, float, Number]
ListLike = Union[list, _List]
MapLike = Union[dict, Map]
AnyLike = Union[BoolLike, NullLike, StringLike, NumberLike, ListLike, MapLike]

TfAtomic = Union[BoolLike, NullLike, StringLike, NumberLike]
TfJson = Union[TfAtomic, Dict[str, 'TfJson'], List['TfJson']]
TfJsonObject = Dict[str, TfJson]
TfJsonArray = List[TfJson]
