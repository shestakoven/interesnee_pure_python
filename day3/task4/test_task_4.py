from unittest import TestCase

from day3.task4.task_4 import move


class TestTask4(TestCase):
    def test_normal_shift_right(self):
        result = move(54321, 1)
        self.assertEqual(54132, result)

    def test_normal_shift_left(self):
        result = move(54321, -1)
        self.assertEqual(54213, result)

    def test_str(self):
        result = move('abcde', -1)
        self.assertEqual('Number must be integer', result)
