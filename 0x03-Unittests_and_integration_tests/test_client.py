#!/usr/bin/env python3
"""
Tasks

9. Integration tests

Implement the test_public_repos method to test GithubOrgClient.public_repos.

Make sure that the method returns the expected results based on the fixtures.

Implement test_public_repos_with_license to test the public_repos with the
argument license="apache-2.0" and make sure the result matches the expected
value from the fixtures.
"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock, PropertyMock
from typing import (Dict, Any)


GithubOrgClient = __import__("client").GithubOrgClient
TEST_PAYLOAD = __import__("fixtures").TEST_PAYLOAD


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

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: Any):
        """
        Unit test for the public_repos method of the GithubOrgClient class
        """
        mock_get_json.return_value = [
                {"name": "episodes.dart"}, {"name": "cpp-netlib"},
                {"name": "dagger"}, {"name": "ios-webkit-debug-proxy"}]
        expected_repos = ["episodes.dart", "cpp-netlib", "dagger",
                          "ios-webkit-debug-proxy"]
        repos_url = "https://api.github.com/orgs/google/repos"

        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_property:
            mock_property.return_value = repos_url

            test_instance = GithubOrgClient("google")
            results = test_instance.public_repos()

        self.assertEqual(results, expected_repos)
        mock_get_json.assert_called_once()
        mock_property.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_license(self, repo: Dict, license_key: str,
                         has_license: bool):
        """
        Unittest for GithubOrgClient static method `has_license`
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, has_license)


@parameterized_class(
        ("org_payload", "repos_payload", "expected_repos", "apache2_repos"), [
            (TEST_PAYLOAD[0][0], TEST_PAYLOAD[0][1], TEST_PAYLOAD[0][2],
             TEST_PAYLOAD[0][3])
            ])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test for the GithubOrgClient.public_repos method
    """

    def side_effect(self, url: str):
        """
        Returns the correct repo's json based on the url passed
        """
        for repo in self.repos_payload:
            if repo["url"] == url:
                return repo

    @classmethod
    def setUpClass(cls):
        """
        Mocks `requests.get` to return example payloads found in the fixtures
        """
        cls.get_patcher = patch("requests.get")
        cls.get_patcher.start()
        cls.get_patcher.side_effect = cls.side_effect

    @classmethod
    def tearDownClass(cls):
        """
        Stops the patcher started in the setUpClass method
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Unit test for the GithubOrgClient.public_repos
        """
        with patch("client.GithubOrgClient.repos_payload",
                   new_callable=PropertyMock) as mock_repos:
            mock_repos.return_value = self.repos_payload
            test_instance = GithubOrgClient("google")

            result = test_instance.public_repos()
        mock_repos.assert_called_once()
        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Unittest for the GithubOrgClient.public_repos with the argument
        license="apache-2.0"
        """
        with patch("client.GithubOrgClient.repos_payload",
                   new_callable=PropertyMock) as mock_repos:
            mock_repos.return_value = self.repos_payload
            test_instance = GithubOrgClient("google")
            result = test_instance.public_repos(license="apache-2.0")

        with patch("client.GithubOrgClient.public_repos",
                   return_value=result) as mock_public_repos:
            test_instance2 = GithubOrgClient("google")
            test_instance2.public_repos(license="apache-2.0")

        self.assertEqual(result, self.apache2_repos)
        mock_repos.assert_called_once()
        mock_public_repos.assert_called_once_with(license="apache-2.0")

    # def test_has_license(self):
    #    """
    #    Unittest for the GithubOrgClient.has_license with the argument
    #    license="apache-2.0"
    #    """
    #    result = [repo["name"] for repo in self.repos_payload if
    #              GithubOrgClient.has_license(repo, "apache-2.0")]
    #    self.assertEqual(result, self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
