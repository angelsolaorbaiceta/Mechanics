import operator
from functools import reduce
from typing import List

from geom2d import are_close_enough
from utils.lists import list_of_zeros


class Vector:
    """
    A Vector is a unidimensional array of numbers.

    Upon initialization, the vector is filled with zeroes.
    """

    def __init__(self, length: int):
        self.__length = length
        self.__data = list_of_zeros(length)

    @property
    def length(self):
        """
        Number of values in the vector.

        :return: `int`
        """
        return self.__length

    @property
    def sum(self):
        """
        Sum of all the values in the vector.

        :return: `float`
        """
        return reduce(operator.add, self.__data)

    def set_value(self, value: float, index: int):
        """
        Sets the given `value` in the vector at the position
        indicated by `index`.

        If a value was already set at the given index, it'll be
        overwritten.

        If the index is out of bounds, an error will be raised.

        :param value: `float`
        :param index: `int`
        :return: this vector
        """
        self.__data[index] = value
        return self

    def add_to_value(self, amount: float, index: int):
        """
        Adds the given `amount` to the existing value at the
        position indicated by `index`.

        If the index is out of bounds, an error will be raised.

        :param amount: `float`
        :param index: `int`
        :return: this vector
        """
        self.__data[index] += amount
        return self

    def set_data(self, data: List[float]):
        """
        Sets the given list of `float` numbers ans the values of
        the vector.

        If the size of the list and the length of this vector don't
        match, an error is raised.

        :param data: `[float]` with the values
        :return: this vector
        """
        if len(data) != self.__length:
            raise ValueError('Cannot set data: length mismatch')

        for i in range(self.__length):
            self.__data[i] = data[i]

        return self

    def value_at(self, index: int):
        """
        Returns the value at the position indicated by `index`.

        :param index: `int`
        :return: value at index
        """
        return self.__data[index]

    def scaled(self, factor: float):
        """
        Returns a new vector result of scaling every number by a
        given factor.

        :param factor: `float`
        :return: new vector with the scaled values
        """
        result = self.copy()
        for i in range(self.__length):
            result.__data[i] *= factor

        return result

    def __sub__(self, other):
        """
        Creates a new vector result of subtracting `other` vector
        from this one: this - other.

        :param other: `Vector`
        :return: vector result of subtraction
        """
        if other.__length != self.__length:
            raise ValueError('Cannot subtract: length mismatch')

        result = self.copy()
        for i in range(self.__length):
            result.__data[i] -= other.__data[i]

        return result

    def __add__(self, other):
        """
        Creates a new vector result of adding `other` vector to
        this one: this + other.

        :param other: `Vector`
        :return: vector result of addition
        """
        if other.__length != self.__length:
            raise ValueError('Cannot add: length mismatch')

        result = self.copy()
        for i in range(self.__length):
            result.__data[i] += other.__data[i]

        return result

    def __mul__(self, other):
        """
        Creates a new vector result of multiplying this and other
        vector values one by one.

        :param other: `Vector`
        :return: vector result of multiplication
        """
        if other.__length != self.__length:
            raise ValueError('Cannot multiply: length mismatch')

        result = self.copy()
        for i in range(self.__length):
            result.__data[i] *= other.__data[i]

        return result

    def copy(self):
        """
        Creates a copy of this vector.

        :return: new `Vector`
        """
        return Vector(self.__length).set_data(self.__data.copy())

    def __eq__(self, other):
        """
        Two vectors are considered equal if they contain the same
        values at exactly the same position.

        :param other: `Vector`
        :return: whether the vectors are equal or not
        """
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
