from unittest import TestCase

from day5.task0 import day5_task_0

dd = {'answer': 42, 'foo': {'bar': 'foobar'}}


class TestReadOnlyDict(TestCase):

    def setUp(self) -> None:
        self.d = day5_task_0.ReadOnlyDict(dd.copy())

    def test_normal(self):
        self.assertEqual(42, self.d.answer)

    def test_nested_normal(self):
        self.assertEqual('foobar', self.d.foo.bar)

    def test_edit_item(self):
        with self.assertRaises(PermissionError):
            self.d.answer = 40

    def test_add_item(self):
        with self.assertRaises(PermissionError):
            self.d.x = 'y'

    def test_delete_item(self):
        with self.assertRaises(PermissionError):
            del self.d.answer

    def test_read_invalid_key(self):
        with self.assertRaises(KeyError):
            print(self.d.x)


class TestReadAndModifyDict(TestCase):

    def setUp(self) -> None:
        self.d = day5_task_0.ReadAndModifyDict(dd.copy())

    def test_normal(self):
        self.assertEqual(42, self.d.answer)

    def test_nested_normal(self):
        self.assertEqual('foobar', self.d.foo.bar)

    def test_edit_item(self):
        self.d.answer = 40
        self.assertEqual(40, self.d.answer)
        self.d.answer = 42

    def test_add_item(self):
        with self.assertRaises(PermissionError):
            self.d.x = 'y'

    def test_delete_item(self):
        with self.assertRaises(PermissionError):
            del self.d.answer

    def test_read_invalid_key(self):
        with self.assertRaises(KeyError):
            print(self.d.x)


class TestRMDDict(TestCase):

    def setUp(self) -> None:
        self.d = day5_task_0.RMDDict(dd.copy())

    def test_normal(self):
        self.assertEqual(42, self.d.answer)

    def test_nested_normal(self):
        self.assertEqual('foobar', self.d.foo.bar)

    def test_edit_item(self):
        self.d.answer = 40
        self.assertEqual(40, self.d.answer)
        self.d.answer = 42

    def test_add_item(self):
        with self.assertRaises(PermissionError):
            self.d.x = 'y'

    def test_delete_item(self):
        del self.d.answer
        self.assertNotIn('42', str(self.d))

    def test_read_invalid_key(self):
        with self.assertRaises(KeyError):
            print(self.d.x)


class TestDotMap(TestCase):

    def setUp(self) -> None:
        self.d = day5_task_0.DotMap(dd.copy())

    def test_normal(self):
        self.assertEqual(42, self.d.answer)

    def test_nested_normal(self):
        self.assertEqual('foobar', self.d.foo.bar)

    def test_edit_item(self):
        self.d.answer = 40
        self.assertEqual(40, self.d.answer)

    def test_add_item(self):
        self.d.x = 'y'
        self.assertEqual('y', self.d.x)

    def test_delete_item(self):
        del self.d.answer
        self.assertNotIn('42', str(self.d))

    def test_read_invalid_key(self):
        with self.assertRaises(KeyError):
            print(self.d.x)


class TestProtectedKeysDict(TestCase):

    def setUp(self) -> None:
        self.d = day5_task_0.ProtectKeysDotMap(dd.copy(), protected='answer')

    def test_protected(self):
        with self.assertRaises(PermissionError):
            print(self.d.answer)

    def test_nested_normal(self):
        self.assertEqual('foobar', self.d.foo.bar)

    def test_edit_item(self):
        with self.assertRaises(PermissionError):
            self.d.answer = 40

    def test_add_item(self):
        self.d.x = 'y'
        self.assertEqual('y', self.d.x)

    def test_delete_item(self):
        with self.assertRaises(PermissionError):
            del self.d.answer

    def test_read_invalid_key(self):
        with self.assertRaises(KeyError):
            print(self.d.x)
