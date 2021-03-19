from unittest import TestCase

from day5.task2.main import Matrix, DimensionError


class TestMatrix(TestCase):

    def setUp(self) -> None:
        self.matrix_a = Matrix([0, 1], [2, 3])
        self.matrix_b = Matrix([3, 4], [5, 6])

    def test_create_invalid_matrix(self):
        with self.assertRaises(DimensionError):
            Matrix([1], [2, 3], [3, 1, 4])

    def test_pass_invalid_row(self):
        with self.assertRaises(TypeError):
            Matrix((1, 2))

    def test_invalid_elements(self):
        with self.assertRaises(TypeError):
            Matrix([1, 2], [0.32, ['a']])

    def test_size(self):
        self.assertTupleEqual((2, 2), self.matrix_a.size)

    def test_T(self):
        self.assertEqual(Matrix([0, 2], [1, 3]),
                         self.matrix_a.T())

    def test_add(self):
        self.assertEqual(Matrix([3, 5], [7, 9]),
                         self.matrix_a + self.matrix_b)

    def test_add_wrong(self):
        with self.assertRaises(TypeError):
            self.matrix_a + 42

    def test_sub(self):
        self.assertEqual(Matrix([-3, -3], [-3, -3]),
                         self.matrix_a - self.matrix_b)

    def test_mul_matrix(self):
        self.assertEqual(Matrix([5, 6], [21, 26]),
                         self.matrix_a * self.matrix_b)

    def test_mul_matrix_wrong(self):
        with self.assertRaises(DimensionError):
            self.matrix_a * Matrix([1], [3])

    def test_mul_num(self):
        self.assertEqual(Matrix([0, 5], [10, 15]),
                         self.matrix_a * 5)

    def test_power(self):
        self.assertEqual(Matrix([22, 39], [78, 139]),
                         self.matrix_a ** 4)

    def test_power_wrong(self):
        with self.assertRaises(AttributeError):
            self.matrix_a ** self.matrix_b
