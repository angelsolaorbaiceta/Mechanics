from functools import reduce

from geom2d import are_close_enough
from utils.lists import list_of_zeros


class Vector:

    def __init__(self, length: int):
        self.__length = length
        self.__data = list_of_zeros(length)

    @property
    def length(self):
        return self.__length

    @property
    def sum(self):
        return reduce(lambda sum, val: sum + val, self.__data)

    def set_value(self, value: float, index: int):
        self.__data[index] = value
        return self

    def add_to_value(self, amount: float, index: int):
        self.__data[index] += amount
        return self

    def set_data(self, data: [float]):
        if len(data) != self.__length:
            raise ValueError('Cannot set data: length mismatch')

        for i in range(self.__length):
            self.__data[i] = data[i]

        return self

    def value_at(self, index: int):
        return self.__data[index]

    def scaled(self, factor):
        result = self.copy()
        for i in range(self.__length):
            result.__data[i] *= factor

        return result

    def __sub__(self, other):
        if other.__length != self.__length:
            raise ValueError('Cannot subtract: length mismatch')

        result = self.copy()
        for i in range(self.__length):
            result.__data[i] -= other.__data[i]

        return result

    def __add__(self, other):
        if other.__length != self.__length:
            raise ValueError('Cannot add: length mismatch')

        result = self.copy()
        for i in range(self.__length):
            result.__data[i] += other.__data[i]

        return result

    def __mul__(self, other):
        if other.__length != self.__length:
            raise ValueError('Cannot multiply: length mismatch')

        result = self.copy()
        for i in range(self.__length):
            result.__data[i] *= other.__data[i]

        return result

    def copy(self):
        return Vector(self.__length).set_data(self.__data.copy())

    def __eq__(self, other):
        if self is other:
            return True

        if not isinstance(other, Vector):
            return False

        if self.__length != other.__length:
            return False

        for i in range(self.length):
            if not are_close_enough(
                    self.value_at(i),
                    other.value_at(i)
            ):
                return False

        return True
