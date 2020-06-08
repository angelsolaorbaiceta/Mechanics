import math
import unittest

from geom2d.vector import Vector


class TestVector(unittest.TestCase):
    u = Vector(1, 2)
    v = Vector(4, 6)

    east = Vector(1, 0)
    west = Vector(-1, 0)
    north_east = Vector(1, 1)
    south_east = Vector(1, -1)

    # <----- Operations -----> #
    def test_plus(self):
        expected = Vector(5, 8)
        actual = self.u + self.v
        self.assertEqual(expected, actual)

    def test_minus(self):
        expected = Vector(-3, -4)
        actual = self.u - self.v
        self.assertEqual(expected, actual)

    # <----- Products -----> #
    def test_dot_product(self):
        expected = 16
        actual = self.u.dot(self.v)
        self.assertAlmostEqual(expected, actual)

    def test_cross_product(self):
        expected = -2
        actual = self.u.cross(self.v)
        self.assertAlmostEqual(expected, actual)

    # <----- Parallel & Perpendicular -----> #
    def test_are_parallel(self):
        self.assertTrue(self.u.is_parallel_to(self.u))

    def test_are_not_parallel(self):
        self.assertFalse(self.u.is_parallel_to(self.v))

    def test_are_perpendicular(self):
        perp = Vector(-2, 1)
        self.assertTrue(self.u.is_perpendicular_to(perp))

    def test_are_not_perpendicular(self):
        self.assertFalse(self.u.is_perpendicular_to(self.v))

    # <----- Angle Value -----> #
    def test_angle_value_of_zero(self):
        actual = self.east.angle_value_to(self.east)
        expected = 0
        self.assertAlmostEqual(expected, actual)

    def test_angle_value_of_pi(self):
        actual = self.east.angle_value_to(self.west)
        expected = math.pi
        self.assertAlmostEqual(expected, actual)

    def test_angle_value_when_angle_positive(self):
        actual = self.east.angle_value_to(self.north_east)
        expected = math.pi / 4
        self.assertAlmostEqual(expected, actual)

    def test_angle_value_when_angle_negative(self):
        actual = self.east.angle_value_to(self.north_east)
        expected = math.pi / 4
        self.assertAlmostEqual(expected, actual)

    # <----- Angle Value -----> #
    def test_angle_when_angle_positive(self):
        actual = self.east.angle_to(self.north_east)
        expected = math.pi / 4
        self.assertAlmostEqual(expected, actual)

    def test_angle_when_angle_negative(self):
        actual = self.east.angle_to(self.south_east)
        expected = -math.pi / 4
        self.assertAlmostEqual(expected, actual)

    # <----- Rotate Angle -----> #
    def test_rotate_zero_radians(self):
        actual = self.east.rotated_radians(0)
        expected = self.east
        self.assertEqual(expected, actual)

    def test_rotate_positive_angle(self):
        sqrt2 = math.sqrt(2)
        actual = self.east.rotated_radians(math.pi / 4)
        expected = Vector(1 / sqrt2, 1 / sqrt2)
        self.assertEqual(expected, actual)

    def test_rotate_negative_angle(self):
        sqrt2 = math.sqrt(2)
        actual = self.east.rotated_radians(-math.pi / 4)
        expected = Vector(1 / sqrt2, -1 / sqrt2)
        self.assertEqual(expected, actual)
