from unittest import TestCase

from day2 import task_4

list_dict = task_4.list_dict


class TestTask4(TestCase):

    def test_normal(self):
        result = task_4.calculate(list_dict)
        self.assertEqual([{'key': 'success', 'value': True, 'count': 2}], result)

    def test_all_different(self):
        result = task_4.calculate([{'a': 1}, {'b': 2}])
        self.assertEqual([], result)

    def test_wrong_data(self):
        result = task_4.calculate({1: 2})
        self.assertEqual(task_4.ERRORS_MSGS['invalid_type'], result)

