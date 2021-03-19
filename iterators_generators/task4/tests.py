from unittest import TestCase

from iterators_generators.task4.task4 import chain


class TestChain(TestCase):
    """Test that chain works correctly."""
    def test_normal(self):
        a = [1, 2]
        b = (i for i in range(3, 5))
        d = chain(a, b)
        self.assertListEqual([1, 2, 3, 4], list(d))

    def test_pass_not_iter(self):
        a = 1
        b = [2, 3]
        c = chain(a, b)
        with self.assertRaises(TypeError):
            list(c)
