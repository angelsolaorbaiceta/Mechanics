import unittest

from structures.parse import parse_bar


class BarParseTest(unittest.TestCase):

    bar_str = '1: (3 -> 5) 25.0 20000000.0'
    nodes_dict = {
        3: 'Node 3',
        5: 'Node 5'
    }
    bar = parse_bar(bar_str, nodes_dict)

    def test_parse_id(self):
        self.assertEqual(1, self.bar.id)

    def test_parse_start_node(self):
        self.assertEqual('Node 3', self.bar.start_node)

    def test_parse_end_node_id(self):
        self.assertEqual('Node 5', self.bar.end_node)

    def test_parse_section(self):
        self.assertEqual(25.0, self.bar.cross_section)

    def test_parse_young_modulus(self):
        self.assertEqual(20000000.0, self.bar.young_mod)
