import math

from eqs.lower_system import solve_lower_sys
from eqs.matrix import Matrix
from eqs.upper_system import solve_upper_sys
from eqs.validate_sys import validate_system
from eqs.vector import Vector


def cholesky_solve(sys_mat: Matrix, sys_vec: Vector) -> Vector:
    """
    The Cholesky factorization method solves systems of linear
    equations whose matrix (`sys_mat`) is positive-definite.

    The Cholesky method decomposes the system matrix `sys_mat`
    into the product of a lower triangular matrix and its
    conjugate transpose.
    This step is done by the `lower_matrix_decomposition` function.

    Then solves the system in two steps:
        - `solve_lower_sys`
        - `solve_upper_sys`

    :param sys_mat: system's `Matrix`
    :param sys_vec: system's vector `Vector`
    :return: result `Vector`
    """
    validate_system(sys_mat, sys_vec)

    low_matrix = lower_matrix_decomposition(sys_mat)
    up_matrix = low_matrix.transposed()
    low_solution = solve_lower_sys(low_matrix, sys_vec)
    return solve_upper_sys(up_matrix, low_solution)


def lower_matrix_decomposition(sys_mat: Matrix) -> Matrix:
    """
    Decomposes the matrix `sys_mat` into the product of a lower
    triangular matrix and its conjugate transpose: [A] = [L][L]'.

    It only returns the lower triangular matrix [L] as the
    transpose can be computed from it.

    :param sys_mat: `Matrix`
    :return: lower triangular `Matrix`
    """
    size = sys_mat.rows_count
    low_mat = Matrix(size, size)

    for i in range(size):
        sq_sum = 0

        for j in range(i + 1):
            m_ij = sys_mat.value_at(i, j)

            if i == j:
                # main diagonal value
                diag_val = math.sqrt(m_ij - sq_sum)
                low_mat.set_value(diag_val, i, j)

            else:
                # value under main diagonal
                non_diag_sum = 0
                for k in range(j):
                    l_ik = low_mat.value_at(i, k)
                    l_jk = low_mat.value_at(j, k)
                    non_diag_sum += l_ik * l_jk

                l_jj = low_mat.value_at(j, j)
                non_diag_val = (m_ij - non_diag_sum) / l_jj
                sq_sum += non_diag_val * non_diag_val

                low_mat.set_value(non_diag_val, i, j)

    return low_mat
