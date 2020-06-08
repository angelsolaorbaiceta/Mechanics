import unittest

from geom2d import Point, Vector
from structures.model.node import StrNode


class NodeTest(unittest.TestCase):

    def test_net_load(self):
        loads = [Vector(10, 20), Vector(30, 40)]
        node = StrNode(1, Point(2, 5), loads)
        expected = Vector(40, 60)
        self.assertEqual(expected, node.net_load)
