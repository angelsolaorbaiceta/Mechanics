import re

__TRANSF_VAL_RE = r'(?P<val>-?\d+(\.\d+)?)'


def parse_transform_term(term, line):
    __ensure_term_name(term, line)
    return __parse_transform_term(line)


def __ensure_term_name(name, line):
    if name not in line:
        raise ValueError(f'Expected {name} term')


def __parse_transform_term(line):
    matches = re.search(__TRANSF_VAL_RE, line)
    if not matches:
        raise ValueError('Couldn\'t read transform term')

    return float(matches.group('val'))
