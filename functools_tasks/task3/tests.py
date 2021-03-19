from unittest import TestCase

from functools_tasks.task3.task3 import process_list


class TestProcessList(TestCase):
    """Tests that filtering and ordering are cool. """
    def test_order(self):
        result = process_list([1, 'c', 'z', 2], order=True)
        self.assertListEqual(['1', '2', 'c', 'z'], result)

    def test_filter(self):
        result = process_list(['1', 'Bz', 'ba'], filter_b=True)
        self.assertListEqual(['ba', 'Bz'], result)


