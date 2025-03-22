import math
import unittest

from geom2d.circle import Circle
from geom2d.point import Point
from geom2d.polygon import Polygon
from geom2d.vector import Vector


class TestCircle(unittest.TestCase):
    circle = Circle(Point(10, 10), 10)

    # --- PROPERTIES --- #
    def test_area(self):
        expected = math.pi * 100
        self.assertAlmostEqual(expected, self.circle.area)

    def test_circumference(self):
        expected = math.pi * 20
        self.assertAlmostEqual(expected, self.circle.circumference)

    # --- CONTAINS --- #
    def test_contains_point(self):
        point = Point(11, 12)
        self.assertTrue(self.circle.contains_point(point))

    def test_doesnt_contain_point(self):
        point = Point(100, 50)
        self.assertFalse(self.circle.contains_point(point))

    # --- OVERLAPS --- #
    def test_overlaps(self):
        other = Circle(Point(30, 30), 20)
        self.assertTrue(self.circle.overlaps(other))

    def test_dont_overlap(self):
        other = Circle(Point(30, 30), 5)
        self.assertFalse(self.circle.overlaps(other))

    # --- PENETRATION --- #
    def test_no_penetration(self):
        other = Circle(Point(30, 30), 5)
        self.assertIsNone(self.circle.penetration_vector(other))

    def test_penetration(self):
        other = Circle(Point(30, 30), 20)
        actual = self.circle.penetration_vector(other)
        pen_proj = -(math.sqrt(2) * 15 - 20)
        expected = Vector(pen_proj, pen_proj)
        self.assertEqual(expected, actual)

    # --- TO POLYGON --- #
    def test_to_polygon_4_divisions(self):
        circle = Circle(Point(2, 5), 10)
        actual = circle.to_polygon(4)
        expected = Polygon([Point(12, 5), Point(2, 15), Point(-8, 5), Point(2, -5)])
        self.assertEqual(expected, actual)
