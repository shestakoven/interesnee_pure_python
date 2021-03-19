from unittest import TestCase

from .main import CustomSet


class TestCustomSet(TestCase):
    """Tests for all methods of CustomSet."""

    def setUp(self):
        self.set = CustomSet([1, 5, 1])

    def test_add(self):
        self.set.add(6)
        self.assertEqual([1, 5, 6], self.set)

    def test_add_same(self):
        self.set.add(1)
        self.assertEqual([1, 5], self.set)

    def test_clear(self):
        self.set.clear()
        self.assertFalse(self.set)

    def test_copy(self):
        copy_set = self.set.copy()
        self.assertEqual(copy_set, self.set)

    def test_difference(self):
        self.assertEqual([5], self.set.difference({1, 3}))

    def test_difference_update(self):
        self.set.difference_update({1, 3})
        self.assertEqual([5], self.set)

    def test_discard(self):
        self.set.discard(5)
        self.set.discard(9)
        self.assertEqual([1], self.set)

    def test_intersection(self):
        new_set = self.set.intersection({5, 2})
        self.assertEqual([5], new_set)

    def test_intersection_update(self):
        self.set.intersection_update({5, 2})
        self.assertEqual([5], self.set)

    def test_isdisjoint_true(self):
        self.assertTrue(self.set.isdisjoint({9, 8}))

    def test_isdisjoint_false(self):
        self.assertFalse(self.set.isdisjoint({1, 8}))

    def test_issubset_true(self):
        self.assertTrue(self.set.issubset({1, 5, 10}))

    def test_issubset_false(self):
        self.assertFalse(self.set.issubset({1, 10}))

    def test_issuperset_true(self):
        self.assertTrue(self.set.issuperset({1}))

    def test_issuperset_false(self):
        self.assertFalse(self.set.issuperset({1, 5, 10}))

    def test_pop(self):
        self.assertEqual(5, self.set.pop())

    def test_pop_with_exc(self):
        with self.assertRaises(KeyError):
            self.set.pop()
            self.set.pop()
            self.set.pop()

    def test_remove(self):
        self.set.remove(1)
        self.assertEqual([5], self.set)

    def test_remove_with_exc(self):
        with self.assertRaises(KeyError):
            self.set.remove(10)

    def test_symmetric_difference(self):
        self.assertEqual([666], self.set.symmetric_difference({1, 5, 666}))

    def test_symmetric_difference_update(self):
        self.set.symmetric_difference_update({1, 5, 666})
        self.assertEqual([666], self.set)

    def test_union(self):
        self.assertEqual([1, 5, 33, 13], self.set.union({13, 33}))

    def test_union_same(self):
        self.assertEqual(self.set, self.set.union({1, 5}))

    def test_update(self):
        self.set.update({13, 33})
        self.assertEqual([1, 5, 13, 33], self.set)

    def test_update_with_same(self):
        self.set.update({1, 5})
        self.assertEqual([1, 5], self.set)

    def test_and(self):
        result = self.set & {1, 7}
        self.assertEqual([1], result)

    def test_contains(self):
        self.assertIn(5, self.set)

    def test_contains_false(self):
        self.assertNotIn(3, self.set)

    def test_eq(self):
        self.assertEqual(self.set, [1, 5])

    def test_eq_false(self):
        self.assertNotEqual(self.set, [1, 5, 3])

    def test_not_eq(self):
        self.assertTrue(self.set != [1, 5, 3])

    def test_ge(self):
        self.assertTrue(self.set >= {1})

    def test_ge_false(self):
        self.assertFalse(self.set >= {1, 5, 3})

    def test_rge(self):
        self.assertTrue({1, 5, 6} >= self.set)

    def test_gt(self):
        self.assertTrue(self.set > {1})

    def test_gt_same_sets(self):
        self.assertFalse(self.set > {1, 5})

    def test_iand(self):
        self.set &= {1, 5, 6, 7}
        self.assertEqual([1, 5], self.set)

    def test_ior(self):
        self.set |= {1, 5, 6, 7}
        self.assertEqual([1, 5, 6, 7], self.set)

    def test_isub(self):
        self.set -= {1, 6, 7}
        self.assertEqual([5], self.set)

    def test_iter(self):
        for item in self.set:
            self.assertTrue(item in [1, 5])

    def test_ixor(self):
        self.set ^= {0, 1, 5, 7}
        self.assertEqual([0, 7], self.set)

    def test_len(self):
        self.assertEqual(2, len(self.set))

    def test_le(self):
        self.assertTrue(self.set <= {1, 4, 5, 7})

    def test_le_false(self):
        self.assertFalse(self.set <= {1, 3, 6})

    def test_lt(self):
        self.assertTrue(self.set < {1, 4, 5, 6})

    def test_lt_false(self):
        self.assertFalse(self.set < {1, 5})

    def test_or(self):
        self.assertEqual([1, 5, 7], self.set | {1, 7})

    def test_sub(self):
        self.assertEqual([5], self.set - {1, 7, 6})

    def test_xor(self):
        self.assertEqual([0, 6], self.set ^ {0, 1, 5, 6})
