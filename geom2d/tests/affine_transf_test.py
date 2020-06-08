import unittest

from geom2d.point import Point
from geom2d.affine_transf import AffineTransform


class TestAffineTransform(unittest.TestCase):
    point = Point(2, 3)
    scale = AffineTransform(2, 5)
    trans = AffineTransform(1, 1, 10, 15)
    shear = AffineTransform(1, 1, 0, 0, 3, 4)

    # APPLICATION #
    def test_scale_point(self):
        expected = Point(4, 15)
        actual = self.scale.apply_to_point(self.point)
        self.assertEqual(expected, actual)

    def test_translate_point(self):
        expected = Point(12, 18)
        actual = self.trans.apply_to_point(self.point)
        self.assertEqual(expected, actual)

    def test_shear_point(self):
        expected = Point(11, 11)
        actual = self.shear.apply_to_point(self.point)
        self.assertEqual(expected, actual)

    # CONCATENATION #
    def test_concatenate_scale_then_translate(self):
        expected = AffineTransform(2, 5, 10, 15)
        actual = self.scale.then(self.trans)
        self.assertEqual(expected, actual)

    def test_concatenate_translate_then_scale(self):
        expected = AffineTransform(2, 5, 20, 75)
        actual = self.trans.then(self.scale)
        self.assertEqual(expected, actual)

    # INVERSE #
    def test_inverse(self):
        transf = AffineTransform(1, 2, 3, 4, 5, 6)
        expected = AffineTransform(1, 1)
        actual = transf.then(transf.inverse())
        self.assertEqual(expected, actual)
