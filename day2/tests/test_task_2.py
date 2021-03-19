from unittest import TestCase

from day2.task_2 import sort_lists


class TestTask2(TestCase):

    def test_normal(self):
        result = sort_lists([1, 2], [7, 3])
        self.assertListEqual([1, 2, 3, 7], result)

    def test_wrong_types(self):
        result = sort_lists({1, 2}, [7, 3])
        self.assertListEqual([1, 2, 3, 7], result)

    def test_symbols(self):
        result = sort_lists(['a', 'b'], ['c', 'd'])
        self.assertListEqual(['a', 'b', 'c', 'd'], result)

    def test_three_lists(self):
        with self.assertRaises(TypeError):
            sort_lists([1], [2], [3])
