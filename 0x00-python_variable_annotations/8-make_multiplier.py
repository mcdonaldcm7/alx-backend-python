#!/usr/bin/env python3
"""
Task
8. Complex types - functions

Write a type-annotated function 'make-multiplier' that takes a float
'multiplier' as argument and returns a function that multiplies a float by
'multiplier'.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return: A callable function
    """
    def times_multiplier(n: float) -> float:
        """
        Returns: multiplier * n
        """
        return multiplier * n
    return times_multiplier
