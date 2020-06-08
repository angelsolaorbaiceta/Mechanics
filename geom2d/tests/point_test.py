import unittest

from geom2d.point import Point


class TestPoint(unittest.TestCase):
    p = Point(1, 2)
    q = Point(4, 6)

    # <----- Distance -----> #
    def test_distance_to(self):
        expected = 5
        actual = self.p.distance_to(self.q)
        self.assertAlmostEqual(expected, actual)

    # <----- Operations -----> #
    def test_plus(self):
        expected = Point(5, 8)
        actual = self.p + self.q
        self.assertEqual(expected, actual)

    def test_minus(self):
        expected = Point(-3, -4)
        actual = self.p - self.q
        self.assertEqual(expected, actual)
