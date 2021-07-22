MIN = 0.0
MIDDLE = 0.5
MAX = 1.0


def make(value: float):
    """
    Creates a valid T parameter value.
    If the given `value` is below the minimum of 0, it returns 0.
    If the given `value` is above the maximum of 1, it returns 1.

    The T parameter is defined in the range [0, 1] inclusive.

    :param value: `float`
    :return: T param
    """
    if value < MIN:
        return MIN

    if value > MAX:
        return MAX

    return value


def ensure_valid(t: float):
    """
    Raises a `TParamError` if `value` is outside the range [0, 1].

    :param t: `float` t parameter value
    """
    if not is_valid(t):
        raise TParamError(t)


def is_valid(t: float) -> bool:
    """
    Returns a `bool` indicating if the given value for a t
    parameter is valid.

    A t parameter is valid if in the [0, 1] range.

    :param t: `float` t parameter value
    :return: `bool` is the t value valid?
    """
    return False if t < MIN or t > MAX else True


class TParamError(Exception):
    """
    Exception that reports a wrong value for the t parameter.
    """

    def __init__(self, t):
        self.t = t

    def __str__(self):
        return f'Expected t to be in [0, 1] but was {self.t}'
