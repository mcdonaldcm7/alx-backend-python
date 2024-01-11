#!/usr/bin/env python3
"""
Task
2. Basic annotations - floor

Write a type-annotated function 'floor' which takes a float 'n' as argument and
returns the floor of the float
"""
import math


def floor(n: float) -> float:
    """
    Returns the floored value of the argument n
    """
    return math.floor(n)
