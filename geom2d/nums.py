import math


def are_close_enough(a, b, tolerance=1e-10):
    return math.fabs(a - b) < tolerance


def is_close_to_zero(a, tolerance=1e-10):
    return are_close_enough(a, 0.0, tolerance)


def is_close_to_one(a, tolerance=1e-10):
    return are_close_enough(a, 1.0, tolerance)


def value_or_zero(a, tolerance=1e-10):
    return 0 if is_close_to_zero(a, tolerance) else a
