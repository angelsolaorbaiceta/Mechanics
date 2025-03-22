from geom2d import make_rect_centered, Circle, Point, Vector
from graphic import svg


def draw_to_svg(points: [Point], circle: Circle, config):
    pt_radius = circle.radius / 20
    svg_output = output_to_svg(circle, config["output"])
    svg_input = input_to_svg(points, pt_radius, config["input"])

    viewbox = make_viewbox(circle)
    svg_img = svg.svg_content(viewbox.size, svg_output + svg_input, viewbox)

    print(svg_img)


def output_to_svg(circle: Circle, config):
    style = style_from_config(config)
    label_style = label_style_from_config(config)

    return [
        svg.circle(circle, style),
        svg.text(f"O {circle.center}", circle.center, Vector(0, 0), label_style),
        svg.text(f"r = {circle.radius}", circle.center, Vector(0, 20), label_style),
    ]


def input_to_svg(points: [Point], point_radius: float, config):
    style = style_from_config(config)
    label_style = label_style_from_config(config)
    [a, b, c] = points
    disp = Vector(1.25 * point_radius, 0)

    return [
        svg.circle(Circle(a, point_radius), style),
        svg.circle(Circle(b, point_radius), style),
        svg.circle(Circle(c, point_radius), style),
        svg.text(f"A {a}", a, disp, label_style),
        svg.text(f"B {b}", b, disp, label_style),
        svg.text(f"C {c}", c, disp, label_style),
    ]


def style_from_config(config):
    return [
        svg.stroke_color(config["stroke-color"]),
        svg.stroke_width(config["stroke-width"]),
        svg.fill_color(config["fill-color"]),
    ]


def label_style_from_config(config):
    return [
        svg.font_size(config["label-size"]),
        svg.font_family(config["font-family"]),
        svg.fill_color(config["stroke-color"]),
    ]


def make_viewbox(circle: Circle):
    height = 2.5 * circle.radius
    width = 4 * circle.radius
    return make_rect_centered(circle.center, width, height)
