from unittest import TestCase

from functools_tasks.task5.task5 import get_comb_len_2


class TestGetCombinations(TestCase):

    def test_integers_input(self):
        result = get_comb_len_2([1, 2])
        self.assertListEqual([(1, 1), (1, 2), (2, 1), (2, 2)], result)

    def test_strings_input(self):
        result = get_comb_len_2(['a', 'b'])
        self.assertListEqual([('a', 'a'), ('a', 'b'), ('b', 'a'), ('b', 'b')], result)
