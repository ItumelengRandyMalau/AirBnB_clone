#!/usr/bin/python3
"""Unit tests for the User class"""

import unittest
from models.user import User


class TestUserAttributes(unittest.TestCase):
    """Unittests for testing instantiation of the User class"""
    def setUp(self):
        self.user = User()

    def test_email_attribute(self):
        self.assertEqual(self.user.email, "")

        # Assign a value to email attribute
        self.user.email = "test@example.com"
        self.assertEqual(self.user.email, "test@example.com")

    def test_password_attribute(self):
        self.assertEqual(self.user.password, "")

        # Assign a value to password attribute
        self.user.password = "password123"
        self.assertEqual(self.user.password, "password123")

    def test_first_name_attribute(self):
        self.assertEqual(self.user.first_name, "")

        # Assign a value to first_name attribute
        self.user.first_name = "John"
        self.assertEqual(self.user.first_name, "John")

    def test_last_name_attribute(self):
        self.assertEqual(self.user.last_name, "")

        # Assign a value to last_name attribute
        self.user.last_name = "Doe"
        self.assertEqual(self.user.last_name, "Doe")


if __name__ == '__main__':
    unittest.main()
