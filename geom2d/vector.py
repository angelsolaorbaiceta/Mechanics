import math

from geom2d import nums


class Vector:
    """
    Vector is a direction in the 2D plane, defined by its two
    projections: `u` and `v`.
    """

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
        """
        Returns a new `Vector` result of scaling the `u` and `v`
        projections of this one scaled the given `factor`.

        :param factor: `float`
        :return: `Vector`
        """
        return Vector(factor * self.u, factor * self.v)

    @property
    def sine(self):
        """
        Computes the sine of the angle of this vector with the
        horizontal direction.

        :return: `float` = sin(angle)
        """
        return self.v / self.norm

    @property
    def cosine(self):
        """
        Computes the cosine of the angle of this vector with the
        horizontal direction.

        :return: `float` = cos(angle)
        """
        return self.u / self.norm

    @property
    def norm(self):
        """
        The norm or length of the vector.

        :return: `float`
        """
        return math.sqrt(self.u ** 2 + self.v ** 2)

    @property
    def is_normal(self):
        """
        Boolean indicating whether the vector is normal or not.
        A vector is normal if it has unitary length.

        :return: `bool`
        """
        return nums.is_close_to_one(self.norm)

    def normalized(self):
        """
        Creates a new version of this vector scaled to have
        unit length.

        :return: `Vector`
        """
        return self.scaled_by(1.0 / self.norm)

    def with_length(self, length):
        """
        Creates a new version of this vector scaled to have
        the given `length`.

        :param length: `float`
        :return: `Vector`
        """
        return self.normalized().scaled_by(length)

    def dot(self, other):
        """
        Computes the dot product of this vector and `other`.

        :param other: `Vector`
        :return: `float`
        """
        return (self.u * other.u) + (self.v * other.v)

    def cross(self, other):
        """
        Computes the cross product of this vector and `other`.

        :param other: `Vector`
        :return: `float`
        """
        return (self.u * other.v) - (self.v * other.u)

    def is_parallel_to(self, other):
        """
        Tests whether a vector `other` is parallel to this one.

        :param other: `Vector`
        :return: `bool`
        """
        return nums.is_close_to_zero(
            self.cross(other)
        )

    def is_perpendicular_to(self, other):
        """
        Tests whether a vector `other` is perpendicular to this
        one.

        :param other: `Vector`
        :return: `bool`
        """
        return nums.is_close_to_zero(
            self.dot(other)
        )

    def angle_value_to(self, other):
        """
        Computes the absolute value of the angle in radians between
        this vector and `other`.

        :param other: `Vector`
        :return: `float` angle in radians
        """
        dot_product = self.dot(other)
        norm_product = self.norm * other.norm
        return math.acos(dot_product / norm_product)

    def angle_to(self, other):
        """
        Computes the value (including the sign) of the angle in
        radians between this vector and `other`.

        :param other: `Vector`
        :return: `float` angle in radians
        """
        value = self.angle_value_to(other)
        cross_product = self.cross(other)
        return math.copysign(value, cross_product)

    def rotated_radians(self, radians):
        """
        Computes a new `Vector` result of rotating this vector a
        given angle in radians.

        :param radians: `float` angle in radians
        :return: `Vector`
        """
        cos = math.cos(radians)
        sin = math.sin(radians)
        return Vector(
            self.u * cos - self.v * sin,
            self.u * sin - self.v * cos
        )

    def perpendicular(self):
        """
        Creates a vector perpendicular to this one. The result is
        the same as rotating this vector 90º.

        :return: `Vector`
        """
        return Vector(-self.v, self.u)

    def opposite(self):
        """
        Creates a vector collinear but with opposite direction than
        this one.

        :return: `Vector`
        """
        return Vector(-self.u, -self.v)

    def projection_over(self, direction):
        """
        Computes the projection length of this vector over the
        given `direction`.

        :param direction: `Vector`
        :return: `float` length of the projection
        """
        return self.dot(direction.normalized())

    def __eq__(self, other):
        """
        Returns a `bool` indicating whether this and `other` vector
        are equal.

        Two `Vector` instances are equal if their projections are
        equal.

        :param other: `Vector`
        :return: `bool`
        """
        if self is other:
            return True

        if not isinstance(other, Vector):
            return False

        return nums.are_close_enough(self.u, other.u) and \
               nums.are_close_enough(self.v, other.v)

    def __str__(self):
        return f'({self.u}, {self.v}) with norm {self.norm}'

    def to_formatted_str(self, decimals: int):
        """
        Returns a string of the form: '(u, v) with norm N', where
        `u` and `v` are the components of the vector and `N` the
        norm.

        All numbers are rounded to the passed in number of
        decimals.

        :param decimals: number of decimals
        :return: '(u, v) with norm N' string
        """
        u = round(self.u, decimals)
        v = round(self.v, decimals)
        norm = round(self.norm, decimals)

        return f'({u}, {v}) with norm {norm}'
