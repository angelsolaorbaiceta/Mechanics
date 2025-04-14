import unittest
from operator import attrgetter

from geom2d import Point, Vector
from structures.model.bar import StrBar
from structures.model.node import StrNode
from structures.model.structure import Structure


class StructureTest(unittest.TestCase):
    def setUp(self):
        self.section = 5
        self.young = 2e7
        self.load = Vector(500, -1000)

        self.n_1 = StrNode(1, Point(0, 0))
        self.n_2 = StrNode(2, Point(0, 200))
        self.n_3 = StrNode(3, Point(400, 200), [self.load])
        self.b_12 = StrBar(1, self.n_1, self.n_2, self.section, self.young)
        self.b_23 = StrBar(2, self.n_2, self.n_3, self.section, self.young)
        self.b_13 = StrBar(3, self.n_1, self.n_3, self.section, self.young)

        self.structure = Structure(
            [self.n_1, self.n_2, self.n_3], [self.b_12, self.b_23, self.b_13]
        )

    def test_nodes_count(self):
        self.assertEqual(3, self.structure.nodes_count)

    def test_bars_count(self):
        self.assertEqual(3, self.structure.bars_count)

    def test_loads_count(self):
        self.assertEqual(1, self.structure.loads_count)

    def test_solve_displacements(self):
        self._set_external_constraints()
        solution = self.structure.solve_structure()

        # Make sure the nodes are ordered by their id
        solution.nodes.sort(key=attrgetter("id"))
        node_1, node_2, node_3 = solution.nodes

        # The first and second nodes are XY constrained. No displacement
        self.assertEqual(node_1.original_pos, node_1.displaced_pos)
        self.assertEqual(node_2.original_pos, node_2.displaced_pos)

        # The third node should be displaced in the {+X, -Y} direction
        self.assertGreater(node_3.global_disp.u, 0.0)
        self.assertLess(node_3.global_disp.v, 0.0)

    def test_solve_reactions(self):
        self._set_external_constraints()
        solution = self.structure.solve_structure()

        # Make sure the nodes are ordered by their id
        solution.nodes.sort(key=attrgetter("id"))
        node_1, node_2, node_3 = solution.nodes

        node_1_reaction = solution.reaction_for_node(node_1)
        self.assertAlmostEqual(2000, node_1_reaction.u, delta=0.75)
        self.assertAlmostEqual(1000, node_1_reaction.v, delta=0.75)

        node_2_reaction = solution.reaction_for_node(node_2)
        self.assertAlmostEqual(-2500, node_2_reaction.u, delta=0.75)
        self.assertAlmostEqual(0, node_2_reaction.v, delta=0.75)

        node_3_reaction = solution.reaction_for_node(node_3)
        self.assertEqual(Vector(0, 0), node_3_reaction)

        # The sum of external forces and reactions should be 0 in X and Y
        sum_forces = self.load + node_1_reaction + node_2_reaction + node_3_reaction
        self.assertAlmostEqual(0.0, sum_forces.u, delta=1.0)
        self.assertAlmostEqual(0.0, sum_forces.v, delta=1.0)

    def _set_external_constraints(self):
        self.n_1.dx_constrained = True
        self.n_1.dy_constrained = True
        self.n_2.dx_constrained = True
        self.n_2.dy_constrained = True
