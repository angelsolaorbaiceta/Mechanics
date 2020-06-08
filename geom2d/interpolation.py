import geom2d.tparam as tparam


def uniform_t_sequence(steps):
    return [t / steps for t in range(steps + 1)]


def ease_in_out_t_sequence(steps):
    return [ease_in_out_t(t) for t in uniform_t_sequence(steps)]


def ease_in_out_t(t):
    return t ** 2 / (t ** 2 + (1 - t) ** 2)


def interpolate(vs, ve, t):
    tparam.ensure_valid(t)
    return vs + t * (ve - vs)
