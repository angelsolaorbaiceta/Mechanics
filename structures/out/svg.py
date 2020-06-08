import json

import pkg_resources as res

from geom2d import AffineTransform
from graphic import svg
from structures.solution.structure import StructureSolution
from .bar_svg import bars_to_svg
from .load_svg import loads_to_svg
from .node_svg import nodes_to_svg
from .reaction_svg import node_reactions_to_svg


def structure_solution_to_svg(
        result: StructureSolution,
        settings,
        _config=None,
):
    __validate_settings(settings)
    default_config = __read_config()

    config = {**default_config, **(_config or {})}

    viewbox = result.bounds_rect(
        config['sizes']['margin'],
        settings.scale
    )
    transform = AffineTransform(sx=1, sy=-1, tx=0, ty=0)

    svg_bars = bars_to_svg(result.bars, settings, config)
    svg_nodes = nodes_to_svg(result.nodes, settings, config)
    svg_react = node_reactions_to_svg(result, settings, config)
    svg_loads = loads_to_svg(result.nodes, settings, config)

    return svg.svg_content(
        size=viewbox.size,
        primitives=svg_bars + svg_nodes + svg_react + svg_loads,
        viewbox_rect=viewbox,
        transform=transform
    )


def __read_config():
    config = res.resource_string(__name__, 'config.json')
    return json.loads(config)


def __validate_settings(settings):
    if 'scale' not in settings:
        raise ValueError('"scale" missing in settings')

    if 'disp_scale' not in settings:
        raise ValueError('"disp_scale" missing in settings')

    if 'load_scale' not in settings:
        raise ValueError('"load_scale" missing in settings')

    if 'no_draw_original' not in settings:
        raise ValueError('"no_draw_original" missing in settings')
