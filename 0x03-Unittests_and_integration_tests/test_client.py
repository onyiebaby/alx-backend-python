#!/usr/bin/env python3
"""GithubOrgClient module"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized

class GithubOrgClient:
    """A client for fetching information from Github organizations"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns correct value"""
        mock_get_json.return_value = {"login": org_name}
        client = GithubOrgClient(org_name)
        result = client.org
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )
        self.assertEqual(result, {"login": org_name})

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test that _public_repos_url returns expected URL"""
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/google/repos"
        }
        client = GithubOrgClient("google")
        self.assertEqual(
            client._public_repos_url,
            "https://api.github.com/orgs/google/repos"
        )

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns the correct list of repo names"""
        # Payload returned by get_json
        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = test_payload

        # Patch _public_repos_url to return a fake URL
        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
        ) as mock_url:
            mock_url.return_value = (
                "https://api.github.com/orgs/google/repos"
            )
            client = GithubOrgClient("google")
            result = client.public_repos()

            # Assert the repo list is as expected
            self.assertEqual(result, ["repo1", "repo2", "repo3"])

            # Ensure mocks were called once
            mock_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/google/repos"
            )
