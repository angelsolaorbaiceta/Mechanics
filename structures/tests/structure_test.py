import unittest
from unittest.mock import patch

from eqs import Matrix
from geom2d import Point, Vector
from eqs.vector import Vector as EqVector
from structures.model.node import StrNode
from structures.model.bar import StrBar
from structures.model.structure import Structure


class StructureTest(unittest.TestCase):
    def setUp(self):
        section = 5
        young = 10
        load = Vector(500, -1000)

        self.n_1 = StrNode(1, Point(0, 0))
        self.n_2 = StrNode(2, Point(0, 200))
        self.n_3 = StrNode(3, Point(400, 200), [load])
        self.b_12 = StrBar(1, self.n_1, self.n_2, section, young)
        self.b_23 = StrBar(2, self.n_2, self.n_3, section, young)
        self.b_13 = StrBar(3, self.n_1, self.n_3, section, young)

        self.structure = Structure(
            [self.n_1, self.n_2, self.n_3], [self.b_12, self.b_23, self.b_13]
        )

    def test_nodes_count(self):
        self.assertEqual(3, self.structure.nodes_count)

    def test_bars_count(self):
        self.assertEqual(3, self.structure.bars_count)

    def test_loads_count(self):
        self.assertEqual(1, self.structure.loads_count)

    @patch("structures.model.structure.cholesky_solve")
    def test_assemble_system_matrix(self, cholesky_mock):
        eal3 = 0.1118033989
        c2_eal3 = 0.8 * eal3
        s2_eal3 = 0.2 * eal3
        cs_eal3 = 0.4 * eal3
        expected_mat = Matrix(6, 6).set_data(
            [
                c2_eal3,
                cs_eal3,
                0,
                0,
                -c2_eal3,
                -cs_eal3,
                cs_eal3,
                0.25 + s2_eal3,
                0,
                -0.25,
                -cs_eal3,
                -s2_eal3,
                0,
                0,
                0.125,
                0,
                -0.125,
                0,
                0,
                -0.25,
                0,
                0.25,
                0,
                0,
                -c2_eal3,
                -cs_eal3,
                -0.125,
                0,
                0.125 + c2_eal3,
                cs_eal3,
                -cs_eal3,
                -s2_eal3,
                0,
                0,
                cs_eal3,
                s2_eal3,
            ]
        )

        self.structure.solve_structure()
        [actual_mat, _] = cholesky_mock.call_args[0]

        cholesky_mock.assert_called_once()
        self.assertEqual(expected_mat, actual_mat)

    @patch("structures.model.structure.cholesky_solve")
    def test_system_matrix_constraints(self, cholesky_mock):
        self._set_external_constraints()

        eal3 = 0.1118033989
        c2_eal3 = 0.8 * eal3
        s2_eal3 = 0.2 * eal3
        cs_eal3 = 0.4 * eal3
        expected_mat = Matrix(6, 6).set_data(
            [
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0.125 + c2_eal3,
                cs_eal3,
                0,
                0,
                0,
                0,
                cs_eal3,
                s2_eal3,
            ]
        )

        self.structure.solve_structure()
        [actual_mat, _] = cholesky_mock.call_args[0]

        cholesky_mock.assert_called_once()
        self.assertEqual(expected_mat, actual_mat)

    @patch("structures.model.structure.cholesky_solve")
    def test_assemble_system_vector(self, cholesky_mock):
        expected_vec = EqVector(6).set_data([0, 0, 0, 0, 500, -1000])

        self.structure.solve_structure()
        [_, actual_vec] = cholesky_mock.call_args[0]

        self.assertEqual(expected_vec, actual_vec)

    def test_solve_displacements(self):
        self._set_external_constraints()

        solution = self.structure.solve_structure()
        # TODO

    def _set_external_constraints(self):
        self.n_1.dx_constrained = True
        self.n_1.dy_constrained = True
        self.n_2.dx_constrained = True
        self.n_2.dy_constrained = True
