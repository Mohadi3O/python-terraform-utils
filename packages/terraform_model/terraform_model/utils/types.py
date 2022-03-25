# std
from __future__ import annotations
from typing import Dict, List, Union

JsonPrimitive = Union[int, float, str, bool, None]
Json = Union[JsonPrimitive, Dict[str, 'Json'], List['Json']]
JsonObject = Dict[str, Json]
JsonArray = List[Json]
AnyObject = Dict[str, any]


def is_json_primitive(value: any) -> bool:
    return (
        isinstance(value, int) or
        isinstance(value, float) or
        isinstance(value, str) or
        isinstance(value, bool) or
        value is None
    )
