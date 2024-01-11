#!/usr/bin/env python3
"""
Task
11. More involved type annotations

Given the parameters and the return values, add type annotations to the
function

Hint: look into TypeVar

def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
"""
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Return: The value of key if key exists, else return None
    """
    if key in dct:
        return dct[key]
    else:
        return default
