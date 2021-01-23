from eqs import Matrix, Vector
from eqs.lower_system import solve_lower_sys
from eqs.upper_system import solve_upper_sys


def lu_system_solve(
        lower_matrix: Matrix,
        upper_matrix: Matrix,
        sys_vector: Vector
) -> Vector:
    """
    Given a linear equation system's matrix LU decomposition and
    its system vector, it uses forward and backward substitution
    to compute the system's solution.

    :param lower_matrix:
    :param upper_matrix:
    :param sys_vector:
    :return: vector, system's solution
    """
    low_solution = solve_lower_sys(lower_matrix, sys_vector)
    return solve_upper_sys(upper_matrix, low_solution)
