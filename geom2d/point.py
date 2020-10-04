import math

from geom2d import nums
from geom2d.vector import Vector


class Point:
    """
    Point is a position in the 2D plane, defined by its two
    coordinates: `x` and `y`.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """
        Creates a `Point` result of adding the coordinates of this
        point and `other`.

        This operation doesn't make a lot of algebraic sense, but
        it will be useful for some operations.

        :param other: `Point`
        :return: `Point` sum of `self` and `other`
        """
        return Point(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other):
        """
        Creates a `Vector` going from `other` to `self`.

        :param other: `Point`
        :return: `Vector`: `other` -> `self`
        """
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def distance_to(self, other):
        """
        Computes the distance from this point to `other`.

        :param other: `Point`
        :return: `float` = distance(this, other)
        """
        delta_x = other.x - self.x
        delta_y = other.y - self.y
        return math.sqrt(delta_x ** 2 + delta_y ** 2)

    def displaced(self, vector: Vector, times=1):
        """
        Creates a new `Point` result of displacing this one the
        given `vector` and number of times `times`.

        :param vector: displacement `Vector`
        :param times: times the displacement vector is applied
        :return: `Point`
        """
        scaled_vec = vector.scaled_by(times)
        return Point(
            self.x + scaled_vec.u,
            self.y + scaled_vec.v
        )

    def __eq__(self, other):
        """
        Two points are equal if their coordinates are equal (or
        close enough).

        :param other: `Point`
        :return: are the points equal?
        """
        if self is other:
            return True

        if not isinstance(other, Point):
            return False

        return nums.are_close_enough(self.x, other.x) and \
               nums.are_close_enough(self.y, other.y)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def to_formatted_str(self, decimals: int):
        """
        Returns a string including the coordinates of the point
        rounded to the given number of decimals.

        :param decimals: number of decimals
        :return: `string` representation of the point
        """
        x = round(self.x, decimals)
        y = round(self.y, decimals)

        return f'({x}, {y})'
