import math

from eqs.lu_solve import lu_system_solve
from eqs.matrix import Matrix
from eqs.validate_sys import validate_system
from eqs.vector import Vector


def cholesky_solve(sys_mat: Matrix, sys_vec: Vector) -> Vector:
    """
    The Cholesky factorization method solves systems of linear
    equations whose matrix (`sys_mat`) is positive-definite.

    The Cholesky method decomposes the system matrix `sys_mat`
    into the product of a lower triangular matrix and its
    conjugate transpose: [L][L]'.
    This step is done by the `lower_matrix_decomposition` function.

    Then solves the system in two steps: a forward substitution
    followed by a backward substitution.

    :param sys_mat: system's `Matrix`
    :param sys_vec: system's vector `Vector`
    :return: result `Vector`
    """
    validate_system(sys_mat, sys_vec)

    lower_matrix = lower_matrix_decomposition(sys_mat)
    upper_matrix = lower_matrix.transposed()
    return lu_system_solve(lower_matrix, upper_matrix, sys_vec)


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
