#!/usr/bin/env python3
"""
Tasks

4. Parameterize and patch as decorators

Familiarize yourself with the client.GithubOrgClient class.

In a new test_client.py file, declare the
TestGithubOrgClient(unittest.TestCase) class and implement the test_org method.

This method should test that GithubOrgClient.org returns the correct value.

Use @patch as a decorator to make sure get_json is called once with the
expected argument but make sure it is not executed.

Use @parameterized.expand as a decorator to parametrize the test with a couple
of org examples to pass to GithubOrgClient, in this order:

    - google
    - abc

Of course, no external HTTP calls should be made.
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
from typing import (Dict, Any)


GithubOrgClient = __import__("client").GithubOrgClient
get_json = __import__("utils").get_json


class TestGithubOrgClient(unittest.TestCase):
    """
    """
    def side_effect(self, arg: Dict) -> Dict:
        """
        Returns the argument passed
        """
        return arg

    @parameterized.expand([
        ("google"),
        ("abc")
        ])
    @patch("utils.get_json")
    def test_org(self, org: str, mock_get_json: Any):
        """
        """
        test_instance = GithubOrgClient(org)

        self.assertIsInstance(test_instance.org, dict)

        url = "https://api.github.com/orgs/{}".format(org)
        mock_get_json.assert_called_once_with(url)
