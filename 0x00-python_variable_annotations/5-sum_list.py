#!/usr/bin/env python3
"""
Task
5. Complex types - list of floats

Write a type-annotated function 'sum_list' which takes a list input_list of
floats as argument and returns their sum as float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Return: sum of float in input_list
    """
    return sum(input_list)
