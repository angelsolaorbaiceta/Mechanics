from apps.aff_transf_motion.parse_geom import *
from apps.aff_transf_motion.parse_transform import parse_transform_term
from geom2d import AffineTransform


def read_input():
    transform = __read_transform()
    primitives = __read_primitives()
    return transform, primitives


def __read_transform():
    return AffineTransform(
        sx=parse_transform_term('sx', input()),
        sy=parse_transform_term('sy', input()),
        shx=parse_transform_term('shx', input()),
        shy=parse_transform_term('shy', input()),
        tx=parse_transform_term('tx', input()),
        ty=parse_transform_term('ty', input())
    )


def __read_primitives():
    prims = {'circs': [], 'rects': [], 'polys': [], 'segs': []}
    has_more_lines = True

    while has_more_lines:
        try:
            line = input()

            if can_parse_circle(line):
                prims['circs'].append(parse_circle(line))

            elif can_parse_rect(line):
                prims['rects'].append(parse_rect(line))

            elif can_parse_polygon(line):
                prims['polys'].append(parse_polygon(line))

            elif can_parse_segment(line):
                prims['segs'].append(parse_segment(line))

        except EOFError:
            has_more_lines = False

    return prims
