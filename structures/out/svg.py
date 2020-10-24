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
    """
    Creates the content of the SVG diagram that depicts the
    structure solution passed as first argument.

    The settings dictionary should contain the different scales
    used for plotting the different parts of the diagram:

    - `disp_scale`: scale used in the displacements.
    - `load_scale`: scale used for drawing loads.
    - `scale`: scale used for the drawing as a whole.
    - `no_draw_original`: used to decide whether to draw the
      original geometry or not.

    :param result: structure solution
    :param settings:
    :param _config:
    :return: SVG
    """

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


__expected_settings = (
    # scale applied to the diagram
    'scale',
    # scale applied to the node displacements
    'disp_scale',
    # scale applied to the load vectors
    'load_scale',
    # boolean to decide whether to draw the original geometry
    'no_draw_original'
)


def __validate_settings(settings):
    for setting in __expected_settings:
        if setting not in settings:
            raise ValueError(f'"{setting}" missing in settings')
