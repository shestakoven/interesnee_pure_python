from unittest import TestCase

from day2.task_5 import merge_dicts

d1 = {'glasses': 1, 'hat': 2}
d2 = {'glasses': 2, 'umbrella': 3, 'hat': 3}
d_right = {'glasses': 2, 'hat': 3, 'umbrella': 3}


class TestMergeDicts(TestCase):
    def test_normal(self):
        result = merge_dicts(d1, d2)
        self.assertDictEqual(d_right, result)

    def test_not_dict(self):
        result = merge_dicts([1, 2, 3])
        self.assertEqual(f'{[1, 2, 3]} is not dict', result)
