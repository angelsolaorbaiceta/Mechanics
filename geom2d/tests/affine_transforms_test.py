import math
import unittest

from geom2d.affine_transf import AffineTransform
from geom2d.affine_transforms import make_rotation
from geom2d.point import Point


class TestAffineTransformations(unittest.TestCase):
    point = Point(7, 2)
    center = Point(2, 2)

    def test_make_positive_rotation(self):
        actual = make_rotation(math.pi / 2, self.center)
        expected = AffineTransform(0, 0, 4, 0, -1, 1)
        self.assertEqual(expected, actual)
