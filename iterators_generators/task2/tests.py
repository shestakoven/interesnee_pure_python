from unittest import TestCase

from iterators_generators.task2.task2 import ReverseIter


class TestReverseIter(TestCase):
    """Test that ReverseIter works correctly."""
    def test_normal(self):
        result = list()
        for num in ReverseIter([1, 2, 3, 4]):
            result.append(num)
        self.assertListEqual([4, 3, 2, 1], result)
