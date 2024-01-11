#!/usr/bin/env python3
"""
Task
9. Let's duck type an iterable object

Annotate the below function's parameter and return values with the appropriate
types

    def element_length(lst):
        return [(i, len(i)] for i in lst]
"""
from typing import Iterable, Sequence, Tuple, Any, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return: List of tuple of elements int lst and length of those elements
    """
    return [(i, len(i)) for i in lst]
