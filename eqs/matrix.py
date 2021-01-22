from eqs import Vector
from geom2d import are_close_enough
from utils.lists import list_of_list_of_zeros


class Matrix:
    """
    A matrix is a n x m array of numbers, where `n` is the number
    of rows and `m` the number of columns.

    Upon initialization, the matrix is filled with zeroes.
    """

    def __init__(self, rows_count: int, cols_count: int):
        self.__rows_count = rows_count
        self.__cols_count = cols_count
        self.__is_square = rows_count == cols_count
        self.__data = list_of_list_of_zeros(rows_count, cols_count)

    @property
    def rows_count(self):
        """
        Number of rows in the matrix.

        :return: `int`
        """
        return self.__rows_count

    @property
    def cols_count(self):
        """
        Number of columns in the matrix.

        :return: `int`
        """
        return self.__cols_count

    @property
    def is_square(self):
        """
        A matrix is square if it has the same number of rows and
        columns.

        :return: `bool`
        """
        return self.__is_square

    def set_value(self, value: float, row: int, col: int):
        """
        Sets the given `value` in the matrix at the position
        indicated by `row` and `column` indices.

        If a value was already set at the given position, it'll be
        overwritten.

        If any of the row or column indices is out of bounds, an
        error will be raised.

        :param value: `float`
        :param row: `int` row index
        :param col: `int` column index
        :return: this matrix
        """
        self.__data[row][col] = value
        return self

    def add_to_value(self, amount: float, row: int, col: int):
        """
        Adds the given `amount` to the existing value at the
        position indicated by `row` and `column` indices.

        If any of the row or column indices is out of bounds, an
        error is raised.

        :param amount: `float`
        :param row: `int` row index
        :param col: int` column index
        :return: this matrix
        """
        self.__data[row][col] += amount
        return self

    def set_data(self, data: [float]):
        """
        Sets the given list of `float` numbers as the values of
        the matrix.

        The matrix is filled with the passed in numbers from left
        to right and from top to bottom.
        The length of the passed in list has to be equal to the
        number of values in the matrix: rows x columns.

        If the size of the list doesn't match the matrix number
        of elements, an error is raised.

        :param data: `[float]` with the values
        :return: this `Matrix`
        """
        if len(data) != self.__cols_count * self.__rows_count:
            raise ValueError('Cannot set data: size mismatch')

        for row in range(self.__rows_count):
            offset = self.__cols_count * row
            for col in range(self.__cols_count):
                self.__data[row][col] = data[offset + col]

        return self

    def set_identity_row(self, row: int):
        """
        Sets the row at index `row` as the identity vector, that
        is, all 0s except for a 1 in the main diagonal position
        (`index = row`).

        :param row: `int` row index
        :return: this matrix
        """
        for col in range(self.__cols_count):
            self.__data[row][col] = 1 if row == col else 0

        return self

    def set_identity_col(self, col: int):
        """
        Sets the column at index `col` as the identity vector, that
        is, all 0s except for a 1 in the main diagonal position
        (`index == column`).

        :param col: `int` column index
        :return: this matrix
        """
        for row in range(self.__rows_count):
            self.__data[row][col] = 1 if row == col else 0

        return self

    def value_at(self, row: int, col: int):
        """
        Returns the value at the position indicated by indices
        `row` and `col`.

        :param row: `int` row index
        :param col: `int` column index
        :return: this matrix
        """
        return self.__data[row][col]

    def value_transposed_at(self, row: int, col: int):
        """
        Returns the value at the position indicated by indices
        `row` and `col` as if this matrix was transposed.

        This method is used as a performance improvement to avoid
        creating a new matrix which is the transpose of another
        matrix.

        :param row: `int` row index
        :param col: `int` column index
        :return:
        """
        return self.__data[col][row]

    def transposed(self):
        """
        Creates a new matrix, result of transposing this matrix.

        :return: transposed matrix
        """
        trans_mat = Matrix(self.__cols_count, self.__rows_count)

        for i in range(self.__rows_count):
            for j in range(self.__cols_count):
                trans_mat.__data[j][i] = self.__data[i][j]

        return trans_mat

    def scale(self, factor: float):
        """
        Multiplies in place every value in the matrix times the
        passed `factor`.

        This method mutates the current matrix; it doesn't create
        a new matrix.

        :param factor: `float`
        :return: this matrix
        """
        for i in range(self.__rows_count):
            for j in range(self.__cols_count):
                self.__data[i][j] *= factor

        return self

    def times_vector(self, v: Vector):
        """
        Creates a new `Vector` result of multiplying this `Matrix`
        times the passed `Vector`.

        In oder for the product to be possible, the matrix column
        count and vector length must match.

        The resulting `Vector` has a length equal to this matrix'
        rows count.

        :param v: `Vector`
        :return: `Vector`
        """
        if self.__cols_count != v.length:
            raise ValueError('Size mismatch')

        result = Vector(self.__rows_count)

        for i in range(self.__rows_count):
            product_sum = 0
            for j in range(self.__cols_count):
                product_sum += self.__data[i][j] * v.value_at(j)

            result.set_value(product_sum, i)

        return result

    def __add__(self, other):
        """
        Creates a new `Matrix` result of adding this one with
        `other`.

        The row and column lengths of both matrices need to be
        equal in order for the matrices to be added.

        :param other: `Matrix`
        :return: result of adding this matrix and `other`
        """
        self.__ensure_matches_size(other)

        result = self.copy()

        for i in range(self.__rows_count):
            for j in range(self.__cols_count):
                result.__data[i][j] += other.__data[i][j]

        return result

    def __sub__(self, other):
        """
        Creates a new `Matrix` result of subtracting `other` from
        this one.

        The row and column lengths of both matrices need to be
        equal in order for the matrices to be subtracted.

        :param other: `Matrix`
        :return: result of subtracting `other` from this matrix
        """
        self.__ensure_matches_size(other)

        result = self.copy()

        for i in range(self.__rows_count):
            for j in range(self.__cols_count):
                result.__data[i][j] -= other.__data[i][j]

        return result

    def __ensure_matches_size(self, other):
        if self.__rows_count != other.__rows_count:
            raise ValueError('Row length mismatch')

        if self.__cols_count != other.__cols_count:
            raise ValueError('Column length mismatch')

    def __mul__(self, other):
        """
        Computes a matrix result of multiplying this times `other`.

        Warning: this method has ~O(n3) time complexity.

        In order for this and `other` to be multiplied, the number
        of columns of this and number of rows of `other` need to
        be equal.

        The result matrix has as many rows as this `Matrix` and as
        many columns as `other` .

        :param other: `Matrix`
        :return: result `Matrix`
        """
        if self.__cols_count != other.__rows_count:
            raise ValueError('Size mismatch')

        rows = self.__rows_count
        cols = other.__cols_count
        size = self.__cols_count
        a_data = self.__data
        b_data = other.__data
        result = Matrix(rows, cols)

        for i in range(rows):
            for j in range(cols):
                prod_sum = 0
                for k in range(size):
                    prod_sum += a_data[i][k] * b_data[k][j]

                result.__data[i][j] = prod_sum

        return result

    def copy(self):
        """
        Creates a new `Matrix` with the exact same size and values
        as this one.

        :return: `Matrix`
        """
        matrix = Matrix(self.__rows_count, self.__cols_count)
        for i in range(self.__rows_count):
            for j in range(self.__cols_count):
                matrix.__data[i][j] = self.__data[i][j]

        return matrix

    def __eq__(self, other):
        """
        Two matrices are considered to be equal if they contain
        the same elements at exactly the same position.

        This is a rather expensive computation with a quadratic
        time complexity.

        :param other: `Matrix`
        :return: whether the matrices are equal or not
        """
        if self is other:
            return True

        if not isinstance(other, Matrix):
            return False

        if self.__rows_count != other.rows_count:
            return False

        if self.__cols_count != other.cols_count:
            return False

        for i in range(self.__rows_count):
            for j in range(self.__cols_count):
                if not are_close_enough(
                        self.__data[i][j],
                        other.__data[i][j]
                ):
                    return False

        return True
