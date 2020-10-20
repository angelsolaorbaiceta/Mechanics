import unittest

from eqs.cholesky import lower_matrix_decomposition, \
    solve_lower_sys, solve_upper_sys, cholesky_solve
from eqs.matrix import Matrix
from eqs.vector import Vector


class CholeskyTest(unittest.TestCase):
    sys_matrix = Matrix(4, 4).set_data([
        4.0, -2.0, 4.0, 2.0,
        -2.0, 10.0, -2.0, -7.0,
        4.0, -2.0, 8.0, 4.0,
        2.0, -7.0, 4.0, 7.0
    ])
    low_matrix = Matrix(4, 4).set_data([
        2.0, 0.0, 0.0, 0.0,
        -1.0, 3.0, 0.0, 0.0,
        2.0, 0.0, 2.0, 0.0,
        1.0, -2.0, 1.0, 1.0
    ])
    sys_vec = Vector(4).set_data([20, -16, 40, 28])
    low_solution = Vector(4).set_data([10, -2, 10, 4])
    solution = Vector(4).set_data([1.0, 2.0, 3.0, 4.0])

    def test_lower_matrix_decomposition(self):
        actual = lower_matrix_decomposition(self.sys_matrix)
        self.assertEqual(self.low_matrix, actual)

    def test_lower_system_resolution(self):
        actual = solve_lower_sys(self.low_matrix, self.sys_vec)
        self.assertEqual(self.low_solution, actual)

    def test_upper_system_resolution(self):
        actual = solve_upper_sys(
            self.low_matrix,
            self.low_solution
        )
        self.assertEqual(self.solution, actual)

    def test_solve_system(self):
        actual = cholesky_solve(self.sys_matrix, self.sys_vec)
        self.assertEqual(self.solution, actual)
