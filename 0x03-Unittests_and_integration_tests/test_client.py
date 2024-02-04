#!/usr/bin/env python3
"""
Tasks

5. Mocking a property

memoize turns methods into properties. Read up on how to mock a property (see
resource).

Implement the test_public_repos_url method to unit-test
GithubOrgClient._public_repos_url.

Use patch as a context manager to patch GithubOrgClient.org and make it return
a known payload.

Test that the result of _public_repos_url is the expected one based on the
mocked payload.
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
from typing import (Dict, Any)


GithubOrgClient = __import__("client").GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Unittest for the GithubOrgClient class from the client module
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
        Test for the org method of the GithubOrgClient class
        """
        test_instance = GithubOrgClient(org)
        url = "https://api.github.com/orgs/{}".format(org)

        self.assertIsInstance(test_instance.org, dict)
        # mock_get_json.assert_called_once_with(url)

    @parameterized.expand([
        ("google"),
        ("holberton")
        ])
    def test_public_repos_url(self, org: str):
        """
        Unit test for the _public_repos_url method
        """
        with patch("utils.get_json", new_callable=PropertyMock
                   ) as mock_get_json:
            mock_get_json.return_value = {
                    "repos_url": (
                        "https://api.github.com/orgs/{}/repos".format(org))}
            test_instance = GithubOrgClient(org)
            result = test_instance._public_repos_url
            self.assertEqual(
                    result, "https://api.github.com/orgs/{}/repos".format(org))
