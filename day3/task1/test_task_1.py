from unittest import TestCase

from day3.task1.task_1 import can_be_palindrome


class TestTask1(TestCase):

    def test_normal(self):
        result = can_be_palindrome('ajajcc')
        self.assertTrue(result)

    def test_not_even(self):
        result = can_be_palindrome('abbcc')
        self.assertTrue(result)

    def test_numbers(self):
        result = can_be_palindrome(12332)
        self.assertTrue(result)

    def test_not_palindrome(self):
        result = can_be_palindrome('abc')
        self.assertFalse(result)
