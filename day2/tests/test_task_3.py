from unittest import TestCase

from day2.task_3 import transliterate


class TestTask3(TestCase):

    def test_normal_ru_to_en(self):
        result = transliterate('Эта строка будет подвержена транслитерации?', from_ru=True)
        self.assertEqual('Eta stroka budet podwerzhena transliteracii?', result)

    def test_normal_en_to_ru(self):
        result = transliterate('Eta stroka budet podwerzhena transliteracii?', from_ru=False)
        self.assertEqual('Ета строка будет подвержена транслитерации?', result)

    def test_nums(self):
        result = transliterate('123', from_ru=True)
        self.assertEqual('123', result)

    def test_bool(self):
        with self.assertRaises(AttributeError):
            transliterate(True, from_ru=True)

    def test_other_type(self):
        with self.assertRaises(AttributeError):
            transliterate([], from_ru=True)