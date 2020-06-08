import math

from eqs.matrix import Matrix
from eqs.vector import Vector


def cholesky_solve(sys_mat: Matrix, sys_vec: Vector) -> Vector:
    __validate_system(sys_mat, sys_vec)

    low_matrix = lower_matrix_decomposition(sys_mat)
    low_solution = solve_lower_sys(low_matrix, sys_vec)
    return solve_upper_sys(low_matrix, low_solution)


def __validate_system(sys_matrix: Matrix, sys_vector: Vector):
    if sys_matrix.cols_count != sys_vector.length:
        raise ValueError('Size mismatch between matrix and vector')

    if not sys_matrix.is_square:
        raise ValueError('System matrix must be square')


def lower_matrix_decomposition(sys_mat: Matrix) -> Matrix:
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


def solve_lower_sys(low_mat: Matrix, sys_vector: Vector):
    size = sys_vector.length
    solution = Vector(size)

    for i in range(size):
        _sum = 0.0

        for j in range(i):
            l_ij = low_mat.value_at(i, j)
            y_j = solution.value_at(j)
            _sum += l_ij * y_j

        b_i = sys_vector.value_at(i)
        l_ii = low_mat.value_at(i, i)
        solution_val = (b_i - _sum) / l_ii
        solution.set_value(solution_val, i)

    return solution


def solve_upper_sys(low_matrix: Matrix, low_vector: Vector):
    size = low_vector.length
    last_index = size - 1
    solution = Vector(size)

    for i in range(last_index, -1, -1):
        _sum = 0.0

        for j in range(i + 1, size):
            u_ij = low_matrix.value_transposed_at(i, j)
            x_j = solution.value_at(j)
            _sum += u_ij * x_j

        y_i = low_vector.value_at(i)
        u_ii = low_matrix.value_transposed_at(i, i)
        solution_val = (y_i - _sum) / u_ii
        solution.set_value(solution_val, i)

    return solution
