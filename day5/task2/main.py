from operator import add, sub


class DimensionError(Exception):

    def __init__(self, text):
        self.text = text


class Matrix:
    """Build a matrix object.

    It provides following matrix operations:
    - summing and substructions;
    - multiplication of two matrices;
    - multiplication of matrix and a number;
    - matrix transposing;
    - inplace operations;
    - dimensions check.

    Examples:
        >>> x = Matrix([0, 1], [2, 3])
        >>> x.size
        (2, 2)
        >>> y = x * 2
        >>> x.T()
        [[0, 2], [1, 3]]
    """

    def __init__(self, *args):
        self.validate_args(args)
        self.matrix = list(args)
        if not all(len(self.matrix[0]) == len(item)
                   for item in self.matrix):
            raise DimensionError('The dimension of the rows must be same.')
        self.size = self.get_size()

    @staticmethod
    def validate_args(args):
        for arg in args:
            if not isinstance(arg, list):
                raise TypeError('Rows must be lists.')
            for element in arg:
                if type(element) not in (int, float):
                    raise TypeError('Elements must be numeric.')

    @staticmethod
    def matrix_check(matrix):
        """If arg is not Matrix, raise exception."""
        if not isinstance(matrix, Matrix):
            raise TypeError(f'{matrix} is not instance of Matrix.')

    def get_size(self):
        if self.matrix:
            return len(self.matrix[0]), len(self.matrix)
        else:
            return 0, 0

    def T(self):
        """Returns transposing matrix."""
        return Matrix(*[list(row) for row in zip(*self.matrix)])

    def _operate(self, other, operator):
        """Helper for __add__ and __sub__ operations.

        Don`t use it for multiplies, because it have another rules.

        Args:
            other: Matrix object.
            operator: 'add' or 'sub'.

        Returns:
            Matrix object.
        """

        self.matrix_check(other)
        if self.size != other.size:
            raise DimensionError('The dimension of the matrices must be same.')
        new_matrix = list()
        for rows in zip(self.matrix, other):
            new_matrix_row = list()
            for elem1, elem2 in zip(*rows):
                new_matrix_row.append(operator(elem1, elem2))
            new_matrix.append(new_matrix_row)
        return Matrix(*new_matrix)

    def __add__(self, other):
        """Add matrix according to the matrix rules."""
        return self._operate(other, add)

    def __sub__(self, other):
        """Sub matrix according to the matrix rules."""
        return self._operate(other, sub)

    def __mul__(self, other):
        """Multiply matrix by matrix or matrix by number
         according to the matrix rules.
         """
        if type(other) in [int, float]:
            return Matrix(*[[elem * other for elem in row] for row in self.matrix])

        self.matrix_check(other)
        if self.size[1] != other.size[0]:
            raise DimensionError('The number of columns is not equal to the number of rows')
        zip_b = list(zip(*other))
        return Matrix(*[[sum(ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b))
                         for col_b in zip_b] for row_a in self.matrix])

    def __iter__(self):
        return iter(self.matrix)

    def __pow__(self, power, modulo=None):
        """Raising a matrix to the power."""
        if self.size[0] != self.size[1]:
            raise DimensionError('Matrix rows != matrix columns.')
        new_matrix = self
        while power != 1:
            new_matrix *= self
            power -= 1
        return new_matrix

    def __eq__(self, other):
        return self.matrix == other.matrix

    def __repr__(self):
        return str(self.matrix)

    def __str__(self):
        """Print matrix like matrix."""
        return '\n'.join(map(str, self.matrix))
