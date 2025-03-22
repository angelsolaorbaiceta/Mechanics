import re

from geom2d import Circle, Point, Rect, Size, Segment
from geom2d import make_polygon_from_coords

__NUM_RE = r"\d+(\.\d+)?"

__CIRC_RE = (
    rf"circ (?P<cx>{__NUM_RE}) (?P<cy>{__NUM_RE}) "
    rf"(?P<r>{__NUM_RE})"
)

__RECT_RE = (
    rf"rect (?P<ox>{__NUM_RE}) (?P<oy>{__NUM_RE}) "
    rf"(?P<w>{__NUM_RE}) (?P<h>{__NUM_RE})"
)

__POLY_RE = rf"poly (?P<coords>[\d\s\.]+)"

__SEGM_RE = (
    rf"segm (?P<sx>{__NUM_RE}) (?P<sy>{__NUM_RE}) "
    rf"(?P<ex>{__NUM_RE}) (?P<ey>{__NUM_RE})"
)


def can_parse_circle(line):
    return re.match(__CIRC_RE, line)


def parse_circle(line):
    match = re.match(__CIRC_RE, line)
    return Circle(
        center=Point(float(match.group("cx")), float(match.group("cy"))),
        radius=float(match.group("r")),
    )


def can_parse_rect(line):
    return re.match(__RECT_RE, line)


def parse_rect(line):
    match = re.match(__RECT_RE, line)
    return Rect(
        origin=Point(float(match.group("ox")), float(match.group("oy"))),
        size=Size(float(match.group("w")), float(match.group("h"))),
    )


def can_parse_polygon(line):
    return re.match(__POLY_RE, line)


def parse_polygon(line):
    match = re.match(__POLY_RE, line)
    coords = [float(n) for n in match.group("coords").split(" ")]
    return make_polygon_from_coords(coords)


def can_parse_segment(line):
    return re.match(__SEGM_RE, line)


def parse_segment(line):
    match = re.match(__SEGM_RE, line)
    return Segment(
        start=Point(float(match.group("sx")), float(match.group("sy"))),
        end=Point(float(match.group("ex")), float(match.group("ey"))),
    )
