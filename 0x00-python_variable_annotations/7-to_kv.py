#!/usr/bin/env python3
"""
Task
7. Complex types - string and int/float to tuple

Write a type-annotated function 'to_kv' that takes a string 'k' and an int OR
float 'v' as arguments and returns a tuple. The first element of the tuple is
the string 'k'. The second element is the square of the int/float 'v' and
should be annotated as a float.
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    """
    Return: A tuple with first key k and second key v ** 2
    """
    return (k, v**2)
