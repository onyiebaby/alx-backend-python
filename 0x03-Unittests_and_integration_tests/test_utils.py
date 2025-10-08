#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """Test class for access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        "Test access_nested_map returns expected results"
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])    
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that KeyError is raised for invalid paths."""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertAlmostEqual(str(error.exception), f"'{path[-1]}'")    
    

        