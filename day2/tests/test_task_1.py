from unittest import TestCase
from unittest.mock import Mock

from day2 import task_1


class TestTask1(TestCase):

    def test_normal_int(self):
        result = task_1.get_composition({1, '2', 'test'},
                                        [1, '3'],
                                        {'1': 2, 2: '3'}, use_for=False)
        self.assertEqual(36, result)

    def test_normal_float_with_zero(self):
        result = task_1.get_composition({1, '2', 'test'},
                                        [1, '3'],
                                        {'1': 2, 2: '3.0'}, use_for=False)
        self.assertEqual(36, result)

    def test_normal_float(self):
        result = task_1.get_composition({1, '2', 'test'},
                                        [1, '3'],
                                        {'1': 2, 2: '3.3'}, use_for=False)
        self.assertEqual(39.6, result)

    def test_without_use_for(self):
        with self.assertRaises(TypeError):
            task_1.get_composition(({1, 3, 5}))

    def test_tuple(self):
        with self.assertRaisesRegex(AttributeError, "'tuple' object has no attribute 'pop'"):
            task_1.get_composition((1, 2, 4), {1, 3}, use_for=True)

    def test_bool(self):
        result = task_1.get_composition([True, False], use_for=True)
        self.assertEqual(result, 0)

