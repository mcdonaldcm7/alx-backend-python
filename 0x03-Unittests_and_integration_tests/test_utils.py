#!/usr/bin/env python3
"""
Task

0. Parameterize a unit test

Familiarize yourself with the utils.access_nested_map function and understand
its purpose. Play with it in the Python console to make sure you understand.

In this task you will write the first unit test for utils.access_nested_map.

Create a TestAccessNestedMap class that inherits from unittest.TestCase.

Implement the TestAccessNestedMap.test_access_nested_map method to test that
the method returns what it is supposed to.
"""
import unittest
from parameterized import parameterized
from typing import (Mapping, Sequence, Any)


access_nested_map = __import__("utils").access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Subclass of unittest class to test the `access_nested_map` function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               exp_result: Any):
        """
        Test for the `access_nested_map` return value for valid inputs
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, exp_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
        ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence, exp_result: Any):
        """
        Test for the Exception the 'access_nested_map' function raises
        """
        kwargs = {"nested_map": nested_map, "path": path}
        self.assertRaises(KeyError, access_nested_map, kwargs,
                          "{}".format(path[len(path) - 1]))
