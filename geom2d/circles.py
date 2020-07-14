from geom2d.circle import Circle
from geom2d.segment import Segment


def make_circle_from_points(a, b, c):
    chord_one_bisec = Segment(a, b).bisector
    chord_two_bisec = Segment(b, c).bisector
    center = chord_one_bisec.intersection_with(chord_two_bisec)
    radius = center.distance_to(a)

    return Circle(center, radius)
