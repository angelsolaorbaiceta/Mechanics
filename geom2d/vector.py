import math

from geom2d import nums


class Vector:
    def __init__(self, u, v):
        self.u = u
        self.v = v

    def __add__(self, other):
        return Vector(
            self.u + other.u,
            self.v + other.v
        )

    def __sub__(self, other):
        return Vector(
            self.u - other.u,
            self.v - other.v
        )

    def scaled_by(self, factor):
        return Vector(factor * self.u, factor * self.v)

    def norm(self):
        return math.sqrt(self.u ** 2 + self.v ** 2)

    def is_normal(self):
        return nums.is_close_to_one(self.norm())

    def normalized(self):
        return self.scaled_by(1.0 / self.norm())

    def with_length(self, length):
        return self.normalized().scaled_by(length)

    def dot(self, other):
        return (self.u * other.u) + (self.v * other.v)

    def cross(self, other):
        return (self.u * other.v) - (self.v * other.u)

    def is_parallel_to(self, other):
        return nums.is_close_to_zero(
            self.cross(other)
        )

    def is_perpendicular_to(self, other):
        return nums.is_close_to_zero(
            self.dot(other)
        )

    def angle_value_to(self, other):
        dot_product = self.dot(other)
        norm_product = self.norm() * other.norm()
        return math.acos(dot_product / norm_product)

    def angle_to(self, other):
        value = self.angle_value_to(other)
        cross_product = self.cross(other)
        return math.copysign(value, cross_product)

    def rotated_radians(self, radians):
        cos = math.cos(radians)
        sin = math.sin(radians)
        return Vector(
            self.u * cos - self.v * sin,
            self.u * sin - self.v * cos
        )

    def perpendicular(self):
        return Vector(-self.v, self.u)

    def opposite(self):
        return Vector(-self.u, -self.v)

    def projection_over(self, direction):
        return self.dot(direction.normalized())

    def sine(self):
        return self.v / self.norm()

    def cosine(self):
        return self.u / self.norm()

    def __eq__(self, other):
        if self is other:
            return True

        if not isinstance(other, Vector):
            return False

        return nums.are_close_enough(self.u, other.u) and \
               nums.are_close_enough(self.v, other.v)

    def __str__(self):
        return f'({self.u}, {self.v}) with norm {self.norm()}'

    def to_formatted_str(self, decimals: int):
        u = round(self.u, decimals)
        v = round(self.v, decimals)
        norm = round(self.norm(), decimals)

        return f'({u}, {v}) with norm {norm}'
