#!/usr/bin/env python3
"""
Task

3. Parameterize and patch

Implement the 'TestMemoize(unittest.TestCase)' class with a
'test_memoize method'.

Inside 'test_memoize', define following class

    class TestClass:

        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

Use 'unittest.mock.patch' to mock 'a_method'. Test that when calling
'a_property' twice, the correct result is returned but 'a_method' is only
called once using 'assert_called_once'.
"""
import unittest
import requests
from parameterized import parameterized
from typing import (Mapping, Sequence, Any, Dict)
from unittest.mock import patch, Mock


access_nested_map = __import__("utils").access_nested_map
get_json = __import__("utils").get_json
memoize = __import__("utils").memoize


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


class TestGetJson(unittest.TestCase):
    """
    Subclass of unittest class to test the `get_json` function from the `utils`
    module
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch("requests.get")
    def test_get_json(self, test_url: str, test_return: Dict, mock_get: Any):
        """
        Test for the 'json' method of the response returned by the 'get' method
        of the 'requests' module
        """
        mock = Mock()
        mock.json.return_value = test_return

        mock_get.return_value = mock
        test_payload = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(test_payload, test_return)


class TestMemoize(unittest.TestCase):
    """
    Unit test for the 'memoize' method of the 'utils' module
    """

    def test_memoize(self):
        """
        Test for the correctness of the 'memoize' method of the 'utils' method
        """
        class TestClass:
            """
            Memoize test class
            """
            def a_method(self):
                """
                Returns the integer 42
                """
                return 42

            @memoize
            def a_property(self):
                """
                Call and return the value from 'a_method'
                """
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as mock:
            test_class = TestClass()

            test1 = test_class.a_property
            test2 = test_class.a_property

        mock.assert_called_once()
        self.assertEqual(test1, 42)
        self.assertEqual(test2, 42)
