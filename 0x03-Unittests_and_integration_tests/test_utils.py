#!/usr/bin/env python3
"""Unit tests for utils.py"""

import unittest
from unittest.mock import patch, Mock
from utils import get_json

class TestGetJson(unittest.TestCase):
    """Test case for utils.get_json function."""

    def test_get_json(self):
        """Test that get_json returns expected result with mocked requests.get"""
        test_cases = [
            ("http://example.com", {"payload": True})
            ("http://holberton.io", {"payload": False}),
        ]
        
        for test_url, test_payload in test_cases:
            with patch('utils.requests.get') as mock_get:
                mock_response = Mock ()
                mock_response.json.return_value = test_payload
                mock_get.return_value = mock_response
        
                result = get_json(test_url)

                mock_get.assert_called_once_with(test_url)
                self.assertEqual(result, test_payload)


     
    

        