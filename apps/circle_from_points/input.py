import json
import re

import pkg_resources as res

from geom2d import Point


def read_config():
    config = res.resource_string(__name__, 'config.json')
    return json.loads(config)


def parse_points():
    return (
        __point_from_string(input()),
        __point_from_string(input()),
        __point_from_string(input()),
    )


def __point_from_string(string):
    matches = re.match(r'(?P<x>\d+)\s(?P<y>\d+)', string)
    return Point(
        int(matches.group('x')),
        int(matches.group('y'))
    )
