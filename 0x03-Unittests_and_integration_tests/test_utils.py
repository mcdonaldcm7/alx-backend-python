#!/usrbin/env python3
"""
Task

2. Mock HTTP calls

Familiarize yourself with the 'utils.get_json' function.

Define the 'TestGetJson(unittest.TestCase)' class and implement the
'TestGetJson.test_get_json' method to test that 'utils.get_json' returns the
expected result.

We don’t want to make any actual external HTTP calls. Use 'unittest.mock.patch'
to patch 'requests.get'. Make sure it returns a 'Mock' object with a 'json'
method that returns 'test_payload' which you parametrize alongside the
'test_url' that you will pass to 'get_json' with the following inputs:

    test_url="http://example.com", test_payload={"payload": True}
    test_url="http://holberton.io", test_payload={"payload": False}

Test that the mocked 'get' method was called exactly once (per input) with
'test_url' as argument.

Test that the output of 'get_json' is equal to 'test_payload'.
"""
import unittest
import requests
from parameterized import parameterized
from typing import (Mapping, Sequence, Any, Dict)
from unittest.mock import patch, Mock


access_nested_map = __import__("utils").access_nested_map
get_json = __import__("utils").get_json


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
