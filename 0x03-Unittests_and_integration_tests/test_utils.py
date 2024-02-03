#!/usrbin/env python3
"""
Task

1. Parameterize a unit test

Implement 'TestAccessNestedMap.test_access_nested_map_exception'. Use the
'assertRaises' context manager to test that a 'KeyError' is raised for the
following inputs (use '@parameterized.expand'):
    nested_map={}, path=("a",)
    nested_map={"a": 1}, path=("a", "b")

Also make sure that the exception message is as expected.
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
