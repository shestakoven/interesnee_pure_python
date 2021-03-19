from unittest import TestCase
from unittest.mock import patch

from day3.task3.task_3 import wait_for_cube, check_number


class TestTask3(TestCase):

    @patch('day3.task_3.input')
    def test_normal(self, task_3_input):
        task_3_input.side_effect = [1, 2, 3, 4, 5, 6]
        self.assertEqual('The cube was assembled', wait_for_cube())

    @patch('day3.task_3.input')
    def test_with_7_8(self, task_3_input):
        task_3_input.side_effect = [7, 8, 1, 2, 3, 4, 5, 6]
        self.assertEqual('The cube was assembled', wait_for_cube())

    def test_invalid_input(self):
        self.assertEqual(False, check_number(0))
