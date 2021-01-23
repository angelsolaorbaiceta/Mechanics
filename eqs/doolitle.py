from eqs import Matrix, Vector
from eqs.lu_solve import lu_system_solve
from eqs.validate_sys import validate_system


def doolitle_solve(sys_mat: Matrix, sys_vec: Vector) -> Vector:
    validate_system(sys_mat, sys_vec)

    (lower, upper) = doolitle_decomposition(sys_mat)
    return lu_system_solve(lower, upper, sys_vec)


def doolitle_decomposition(matrix: Matrix) -> (Matrix, Matrix):
    if not matrix.is_square:
        raise ValueError('Can\'t decompose a non-square matrix')

    size = matrix.rows_count
    (lower, upper) = (Matrix(size, size), Matrix(size, size))

    for i in range(size):
        for j in range(size):
            val = matrix.value_at(i, j)

            if i <= j:
                _sum = 0
                for k in range(i):
                    l_ik = lower.value_at(i, k)
                    u_kj = upper.value_at(k, j)
                    _sum += (l_ik * u_kj)

                upper.set_value(val - _sum, i, j)

            if j <= i:
                _sum = 0
                for k in range(j):
                    l_ik = lower.value_at(i, k)
                    u_kj = upper.value_at(k, j)
                    _sum += (l_ik * u_kj)

                u_jj = upper.value_at(j, j)
                lower.set_value((val - _sum) / u_jj, i, j)

    return lower, upper