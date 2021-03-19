from unittest import TestCase

from functools_tasks.task1.task1 import check_items


class TestCheckItems(TestCase):

    def test_all_true(self):
        """Test that all args is True."""
        result = check_items(True, 1, 'test')
        self.assertEqual('All arguments are True', result)

    def test_all_false(self):
        """Test that all args is False."""
        result = check_items('', False, 0)
        self.assertEqual('All arguments are False', result)

    def test_one_true(self):
        """Test that one arg is True"""
        result = check_items('', '', True)
        self.assertEqual('True arguments only [True]', result)
