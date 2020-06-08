MIN = 0.0
MIDDLE = 0.5
MAX = 1.0


def make(value):
    if value < MIN:
        return MIN

    if value > MAX:
        return MAX

    return value


def ensure_valid(t):
    if not is_valid(t):
        raise TParamError(t)


def is_valid(t):
    return False if t < MIN or t > MAX else True


class TParamError(Exception):
    def __init__(self, t):
        self.t = t

    def __str__(self):
        return f'Expected t to be in [0, 1] but was {self.t}'
