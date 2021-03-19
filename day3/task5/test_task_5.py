from unittest import TestCase

from day3.task5.task_5 import fibonacci_num


class TestFibonacci(TestCase):

    def test_normal(self):
        result = fibonacci_num(6)
        self.assertEqual(8, result)

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            fibonacci_num('a')

    def test_less_then_1(self):
        with self.assertRaises(ValueError):
            fibonacci_num(-1)
