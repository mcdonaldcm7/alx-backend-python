#!/usr/bin/env python3
"""
Tasks

7. Parameterize

Implement TestGithubOrgClient.test_has_license to unit-test
GithubOrgClient.has_license.

Parametrize the test with the following inputs

repo={"license": {"key": "my_license"}}, license_key="my_license"
repo={"license": {"key": "other_license"}}, license_key="my_license"
You should also parameterize the expected returned value.
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

    @parameterized.expand([
        ("google"),
        ("abc")
        ])
    @patch("client.get_json")
    def test_org(self, org: str, mock_get_json: Any):
        """
        Test for the org method of the GithubOrgClient class
        """
        mock_get_json.return_value = {
                "url": "https://api.github.com/orgs/{}".format(org)}
        test_instance = GithubOrgClient(org)
        result = test_instance.org
        url = "https://api.github.com/orgs/{}".format(org)

        self.assertIsInstance(test_instance.org, dict)
        mock_get_json.assert_called_once_with(url)
        self.assertEqual(result, {
                "url": "https://api.github.com/orgs/{}".format(org)})

    @parameterized.expand([
        ("google"),
        ("holberton")
        ])
    def test_public_repos_url(self, org: str):
        """
        Unit test for the _public_repos_url method
        """
        with patch("client.get_json", new_callable=PropertyMock
                   ) as mock_get_json:
            mock_get_json.return_value = {
                    "repos_url": (
                        "https://api.github.com/orgs/{}/repos".format(org))}
            test_instance = GithubOrgClient(org)
            result = test_instance._public_repos_url
            self.assertEqual(
                    result, "https://api.github.com/orgs/{}/repos".format(org))

    @parameterized.expand([
        ("google"),
        ("holberton")
        ])
    @patch("client.get_json")
    def test_public_repos(self, org: str, mock_get_json: Any):
        """
        Unit test for the public_repos method of the GithubOrgClient class
        """
        mock_get_json.return_value = [{"name": org.upper()}]
        repos_url = "https://api.github.com/orgs/{}/repos".format(org)

        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_property:
            mock_property.return_value = repos_url

            test_instance = GithubOrgClient(org)
            results = test_instance.public_repos()

        self.assertEqual(results, [org.upper()])
        mock_get_json.assert_called_once()
        mock_property.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_license(self, repo: Dict, license_key: str, has_license: bool):
        """
        Unittest for GithubOrgClient static method `has_license`
        """
        result_has_license = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result_has_license, has_license)
