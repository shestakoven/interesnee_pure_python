from unittest import TestCase

from day2.task_6 import get_different_keys

d1 = {'glasses': 1, 'hat': 2}
d2 = {'glasses': 2, 'umbrella': 3}
res = (['umbrella', 'hat'], ['hat', 'umbrella'])


class Test(TestCase):

    def test_normal(self):
        result = get_different_keys(d1, d2)
        self.assertIn(result, res)

    def test_not_dict(self):
        result = get_different_keys([1, 2, 3])
        self.assertEqual(f'{[1, 2, 3]} is not dict', result)
