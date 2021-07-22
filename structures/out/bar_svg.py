from math import sqrt
from typing import List

from geom2d import Segment, Vector
from graphic import svg
from graphic.svg import attributes
from structures.solution.bar import StrBarSolution
from .captions_svg import caption_to_svg

__I_VERSOR = Vector(1, 0)
__STRESS_DISP = 10
__DECIMAL_POS = 4


def bars_to_svg(bars: List[StrBarSolution], settings, config):
    """
    Creates the list of SVG elements representing the bars.

    :param bars: list of `StrBarSolution`
    :param settings:
    :param config:
    :return: list of SVG elements
    """
    def original_bar_to_svg(_bar: StrBarSolution):
        color = config['colors']['original']
        return __bar_svg(
            _bar.original_geometry,
            color,
            _bar.cross_section
        )

    def bar_to_svg(_bar: StrBarSolution):
        return __bar_svg(
            _bar.final_geometry_scaling_displacement(
                settings.disp_scale
            ),
            bar_color(_bar),
            _bar.cross_section
        )

    def bar_stress_to_svg(_bar: StrBarSolution):
        geometry = _bar.final_geometry_scaling_displacement(
            settings.disp_scale
        )
        normal = geometry.normal_versor
        position = geometry.middle.displaced(normal, __STRESS_DISP)
        angle = geometry.direction_versor.angle_to(__I_VERSOR)

        return caption_to_svg(
            f'σ = {round(_bar.stress, __DECIMAL_POS)}',
            position,
            angle,
            bar_color(_bar),
            config
        )

    def bar_color(_bar: StrBarSolution):
        if _bar.stress >= 0:
            return config['colors']['traction']
        else:
            return config['colors']['compression']

    should_draw_original = not settings.no_draw_original
    original, final, stresses = [], [], []

    for bar in bars:
        if should_draw_original:
            original.append(original_bar_to_svg(bar))
        final.append(bar_to_svg(bar))
        stresses.append(bar_stress_to_svg(bar))

    # Ordering is important to preserve z-depth
    return original + final + stresses


def __bar_svg(geometry: Segment, color: str, cross_section: float):
    section_height = sqrt(cross_section)
    return svg.segment(
        geometry,
        [
            attributes.stroke_color(color),
            attributes.stroke_width(section_height)
        ]
    )
