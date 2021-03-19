from unittest import TestCase

from day3.task2.task_2 import knight_beats_pawn


class TestTask2(TestCase):
    def test_normal(self):
        result = knight_beats_pawn((8, 8), (7, 6))
        self.assertTrue(result)

    def test_normal_cant_beat(self):
        result = knight_beats_pawn((1, 1), (1, 8))
        self.assertFalse(result)

    def test_invalid_coordinates(self):
        with self.assertRaisesRegex(Exception, 'Coordinates cant be greater 8 and less than 1:'):
            knight_beats_pawn((0, 0), (9, 9))

    def test_invalid_type_of_coor(self):
        with self.assertRaisesRegex(Exception, 'Coordinates must be integers:'):
            knight_beats_pawn(('a', 'b'), ('c', 'd'))
