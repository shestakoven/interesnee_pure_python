from itertools import islice
from unittest import TestCase

from iterators_generators.task1.task1 import Yrange, yrange


class TestTask1(TestCase):

    def test_iterator(self):
        """Test that iterator works correctly."""
        test_list = list()
        for num in islice(Yrange(3), 4):
            test_list.append(num)
        self.assertListEqual([1, 2, 3, 1], test_list)

    def test_generator(self):
        """Test that generator works correctly."""
        test_list = list()
        for num in islice(yrange(3), 4):
            test_list.append(num)
        self.assertListEqual([1, 2, 3, 1], test_list)
