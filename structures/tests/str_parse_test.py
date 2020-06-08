import unittest

import pkg_resources as res

from geom2d import Point, Vector
from structures.parse import parse_structure


class StructureParseTest(unittest.TestCase):

    def setUp(self):
        str_bytes = res.resource_string(__name__, 'test_str.txt')
        str_string = str_bytes.decode("utf-8")
        self.structure = parse_structure(str_string)

    def test_parse_nodes_count(self):
        self.assertEqual(3, self.structure.nodes_count)

    def test_parse_nodes(self):
        nodes = self.structure._Structure__nodes
        self.assertEqual(
            Point(0, 0),
            nodes[0].position
        )
        self.assertEqual(
            Point(200, 150),
            nodes[1].position
        )
        self.assertEqual(
            Point(400, 0),
            nodes[2].position
        )

    def test_parse_node_constraints(self):
        nodes = self.structure._Structure__nodes

        self.assertTrue(nodes[0].dx_constrained)
        self.assertTrue(nodes[0].dy_constrained)

        self.assertFalse(nodes[1].dx_constrained)
        self.assertFalse(nodes[1].dy_constrained)

        self.assertFalse(nodes[2].dx_constrained)
        self.assertTrue(nodes[2].dy_constrained)

    def test_parse_bars_count(self):
        self.assertEqual(3, self.structure.bars_count)

    def test_parse_bars(self):
        bars = self.structure._Structure__bars

        self.assertEqual(1, bars[0].start_node.id)
        self.assertEqual(2, bars[0].end_node.id)

        self.assertEqual(2, bars[1].start_node.id)
        self.assertEqual(3, bars[1].end_node.id)

        self.assertEqual(1, bars[2].start_node.id)
        self.assertEqual(3, bars[2].end_node.id)

    def test_parse_loads_count(self):
        self.assertEqual(1, self.structure.loads_count)

    def test_apply_load_to_node(self):
        node = self.structure._Structure__nodes[1]
        self.assertEqual(
            Vector(2500, -3500),
            node.net_load
        )
