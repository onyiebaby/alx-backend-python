#!/usr/bin/env python3
"""Unit tests for utils.py"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import get_json

class TestAccessNestedMap(unittest.TestCase):
    """Test case for the get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test that utils.get_json returns expected results"""
        mock_response = Mock ()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        
        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


     
    

        