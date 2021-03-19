from unittest import TestCase

from functools_tasks.task4.task4 import get_combinations


class TestGetCombinations(TestCase):

    def test_integers_input(self):
        result = get_combinations([1, 2])
        self.assertListEqual([(1, 1), (1, 2), (2, 1), (2, 2)], result)

    def test_strings_input(self):
        result = get_combinations(['a', 'b'])
        self.assertListEqual([('a', 'a'), ('a', 'b'), ('b', 'a'), ('b', 'b')], result)
