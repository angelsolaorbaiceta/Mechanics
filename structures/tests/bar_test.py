import unittest
from math import sqrt

from eqs import Matrix
from geom2d import Point
from structures.model.node import StrNode
from structures.model.bar import StrBar


class BarTest(unittest.TestCase):
    section = sqrt(5)
    young = 5

    node_a = StrNode(1, Point(0, 0))
    node_b = StrNode(2, Point(2, 1))
    bar = StrBar(1, node_a, node_b, section, young)

    def test_global_stiffness_matrix(self):
        expected = Matrix(4, 4).set_data([
            4, 2, -4, -2,
            2, 1, -2, -1,
            -4, -2, 4, 2,
            -2, -1, 2, 1
        ])
        actual = self.bar.global_stiffness_matrix()
        self.assertEqual(expected, actual)
