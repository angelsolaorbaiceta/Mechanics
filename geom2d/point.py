import math

from geom2d import nums


class Point:
    """
    Point is a position in the 2D plane, defined by its two
    coordinates: `x` and `y`.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other):
        return Point(
            self.x - other.x,
            self.y - other.y
        )

    def distance_to(self, other):
        delta_x = other.x - self.x
        delta_y = other.y - self.y
        return math.sqrt(delta_x ** 2 + delta_y ** 2)

    def displaced(self, vector, times=1):
        scaled_vec = vector.scaled_by(times)
        return Point(
            self.x + scaled_vec.u,
            self.y + scaled_vec.v
        )

    def __eq__(self, other):
        if self is other:
            return True

        if not isinstance(other, Point):
            return False

        return nums.are_close_enough(self.x, other.x) and \
               nums.are_close_enough(self.y, other.y)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def to_formatted_str(self, decimals: int):
        x = round(self.x, decimals)
        y = round(self.y, decimals)

        return f'({x}, {y})'
