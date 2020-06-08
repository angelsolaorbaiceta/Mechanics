from geom2d import are_close_enough
from utils.lists import list_of_list_of_zeros


class Matrix:

    def __init__(self, rows_count: int, cols_count: int):
        self.__rows_count = rows_count
        self.__cols_count = cols_count
        self.__is_square = rows_count == cols_count
        self.__data = list_of_list_of_zeros(rows_count, cols_count)

    @property
    def rows_count(self):
        return self.__rows_count

    @property
    def cols_count(self):
        return self.__cols_count

    @property
    def is_square(self):
        return self.__is_square

    def set_value(self, value: float, row: int, col: int):
        self.__data[row][col] = value
        return self

    def add_to_value(self, amount: float, row: int, col: int):
        self.__data[row][col] += amount
        return self

    def set_data(self, data: [float]):
        if len(data) != self.__cols_count * self.__rows_count:
            raise ValueError('Cannot set data: size mismatch')

        for row in range(self.__rows_count):
            offset = self.__cols_count * row
            for col in range(self.__cols_count):
                self.__data[row][col] = data[offset + col]

        return self

    def set_identity_row(self, row: int):
        for col in range(self.__cols_count):
            self.__data[row][col] = 1 if row == col else 0

        return self

    def set_identity_col(self, col: int):
        for row in range(self.__rows_count):
            self.__data[row][col] = 1 if row == col else 0

        return self

    def value_at(self, row: int, col: int):
        return self.__data[row][col]

    def value_transposed_at(self, row: int, col: int):
        return self.__data[col][row]

    def scale(self, factor: float):
        for i in range(self.__rows_count):
            for j in range(self.__cols_count):
                self.__data[i][j] *= factor

        return self

    def __eq__(self, other):
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
