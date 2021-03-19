from unittest import TestCase

from functools_tasks.task2.task2 import update_object


class TestUpdateObject(TestCase):

    def setUp(self) -> None:
        class Obj:
            pass
        self.obj = Obj()

    def test_add_new_attr(self):
        update_object(self.obj, x=1, y=2)
        self.assertDictEqual({'x': 1, 'y': 2}, vars(self.obj))

    def test_update_same_attr(self):
        self.obj.a = 'a'
        update_object(self.obj, a='b')
        self.assertDictEqual({'a': 'a'}, vars(self.obj))
