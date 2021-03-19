from unittest import TestCase

from iterators_generators.task3.task3 import integers


class TestIntegers(TestCase):
    """Test that integers works correctly."""
    def test_normal(self):
        result = list()
        i1 = integers()
        result.append(next(i1))
        i2 = integers()
        result.append(next(i2))
        self.assertListEqual([1, 2], result)
