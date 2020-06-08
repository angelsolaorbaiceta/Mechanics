def list_of_zeros(length: int):
    return [0] * length


def list_of_list_of_zeros(rows: int, cols: int):
    return [list_of_zeros(cols) for _ in range(rows)]
