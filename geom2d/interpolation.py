import geom2d.tparam as tparam


def uniform_t_sequence(steps: int):
    """
    Creates a sequence of t parameters whose values are equally
    spaced and go from 0 to 1 using the given number of steps.

    :param steps: number of steps
    :return: sequence of t values
    """
    return [t / steps for t in range(steps + 1)]


def ease_in_out_t_sequence(steps: int):
    """
    Creates a sequence of t parameters whose values are spaced
    following an ease-out function and fo from 0 to 1 using the
    given number of steps.

    :param steps: number of steps
    :return: sequence of t values
    """
    return [ease_in_out_t(t) for t in uniform_t_sequence(steps)]


def ease_in_out_t(t: float):
    """
    Returns the ease-in function output for a given t value.

    :param t: t value
    :return: t value mapped according to an ease-in function
    """
    return t**2 / (t**2 + (1 - t) ** 2)


def interpolate(vs: float, ve: float, t: float):
    """
    Computes the interpolated value for a given t value given the
    value at `t = 0` (`vs`) and `t = 1` (`ve`).

    :param vs: start value (at `t = 0`)
    :param ve: end value (at `t = 1`)
    :param t: t value
    :return: value at t
    """
    tparam.ensure_valid(t)
    return vs + t * (ve - vs)
