# std
from __future__ import annotations
from typing import Dict, List, Union

JsonAtomic = Union[int, float, str, bool, None]
Json = Union[JsonAtomic, Dict[str, 'Json'], List['Json']]
JsonObject = Dict[str, Json]
JsonArray = List[Json]
AnyObject = Dict[str, any]


def is_json_atomic(value: any) -> bool:
    return (
        isinstance(value, int) or
        isinstance(value, float) or
        isinstance(value, str) or
        isinstance(value, bool) or
        value is None
    )
