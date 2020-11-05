import sys

from geom2d import Vector


def generate_baltimore_structure(
        spans: int,
        span: float, height: float,
        cross_sec: float, young: float,
        node_load: Vector
):
    """
    Generates and prints to the standard output a Baltimore truss
    structure with the given number of spans, span length, height,
    bar resistant properties and a load vector that'll be applied
    in every node.

    :param spans: even number of spans
    :param span: span length
    :param height: truss height
    :param cross_sec: bars cross section
    :param young: bars Young modulus
    :param node_load: load vector applied in every node
    """
    if spans % 2 != 0:
        raise ValueError('Need an even number of spans')

    print(f'# Baltimore truss with {spans} spans\n')
    __generate_nodes(spans, span, height)
    __generate_loads(spans, node_load)
    __generate_bars(spans, cross_sec, young)


def __generate_nodes(spans: int, span: float, height: float):
    print('nodes')

    __generate_lower_nodes(spans, span)
    __generate_middle_nodes(spans, span, height)
    __generate_upper_nodes(spans, span, height)


def __generate_lower_nodes(spans: int, span: float):
    print('# lower nodes')

    half_span = 0.5 * span
    x = 0.0
    
    for i in range(2 * spans + 1):
        node = f'{i + 1}: ({x}, 0.0) '

        if i == 0:
            node += '(xy)'
        elif i == 2 * spans:
            node += '(y)'
        else:
            node += '()'

        print(node)
        x += half_span


def __generate_middle_nodes(
        spans: int,
        span: float,
        height: float
):
    print('# middle nodes')

    start_id = 2 * spans + 2
    x, y = 0.5 * span, 0.5 * height

    for i in range(spans):
        print(f'{start_id + i}: ({x}, {y}) ()')
        x += span


def __generate_upper_nodes(
        spans: int,
        span: float,
        height: float
):
    print('# upper nodes')

    start_id = 3 * spans + 2
    x = span

    for i in range(spans - 1):
        print(f'{start_id + i}: ({x}, {height}) ()')
        x += span


def __generate_loads(spans: int, node_load: Vector):
    print('\nloads')

    nodes_count = 4 * spans
    for i in range(nodes_count):
        print(f'{i + 1} -> ({node_load.u}, {node_load.v})')


def __generate_bars(
        spans: int,
        cross_sec: float,
        young: float
):
    print('\nbars')

    __generate_diagonal_bars(spans, cross_sec, young)
    __generate_vertical_bars(spans, cross_sec, young)
    __generate_horizontal_bars(spans, cross_sec, young)


def __generate_diagonal_bars(
        spans: int,
        cross_sec: float,
        young: float
):
    __generate_zig_zag_bars(spans, cross_sec, young)
    __generate_left_diagonal_bars(spans, cross_sec, young)
    __generate_right_diagonal_bars(spans, cross_sec, young)


def __generate_zig_zag_bars(
        spans: int,
        cross_sec: float,
        young: float
):
    print('# zig-zag bars')

    id_from, id_to = 1, 2 * spans + 2
    decrement = 2 * spans - 1

    for i in range(2 * spans):
        __print_bar(i + 1, id_from, id_to, cross_sec, young)
        if id_from < id_to:
            id_from = id_to
            id_to = id_to - decrement
            decrement -= 1
        else:
            next_id_to = id_from + 1
            id_from = id_to
            id_to = next_id_to


def __generate_left_diagonal_bars(
        spans: int,
        cross_sec: float,
        young: float
):
    print('# left diagonal bars')

    start_id = 2 * spans + 1
    id_from = 3 * spans + 2
    diff = spans - 1

    __print_bar(
        start_id, id_from, id_from - spans, cross_sec, young
    )

    for i in range(1, int(0.5 * spans)):
        __print_bar(
            start_id + i,
            id_from,
            id_from - diff,
            cross_sec,
            young
        )
        id_from += 1


def __generate_right_diagonal_bars(
        spans: int,
        cross_sec: float,
        young: float
):
    print('# right diagonal bars')

    start_id = int(2.5 * spans + 1)
    id_from = int(3.5 * spans + 2)
    diff = spans

    for i in range(int(0.5 * spans) - 1):
        __print_bar(
            start_id + i,
            id_from,
            id_from - diff,
            cross_sec,
            young
        )
        id_from += 1

    __print_bar(
        int(start_id + 0.5 * spans - 1),
        4 * spans,
        3 * spans + 1,
        cross_sec,
        young
    )


def __generate_vertical_bars(
        spans: int,
        cross_sec: float,
        young: float
):
    print('# vertical bars')

    current_id = 3 * spans + 1
    even_diff, uneven_diff = 2 * spans, 3 * spans - 1

    for i in range(2, 2 * spans + 1):
        if i % 2 == 0:
            __print_bar(
                current_id, i, i + even_diff, cross_sec, young
            )
            even_diff -= 1
        else:
            __print_bar(
                current_id, i, i + uneven_diff, cross_sec, young
            )
            uneven_diff -= 1

        current_id += 1


def __generate_horizontal_bars(
        spans: int,
        cross_sec: float,
        young: float
):
    __generate_lower_horizontal_bars(spans, cross_sec, young)
    __generate_upper_horizontal_bars(spans, cross_sec, young)


def __generate_lower_horizontal_bars(
        spans: int,
        cross_sec: float,
        young: float
):
    print('# lower horizontal bars')

    start_id = 5 * spans
    for i in range(2 * spans):
        __print_bar(start_id + i, i + 1, i + 2, cross_sec, young)


def __generate_upper_horizontal_bars(
        spans: int,
        cross_sec: float,
        young: float
):
    print('# upper horizontal bars')

    current_id = 7 * spans
    for i in range(3 * spans + 2, 4 * spans):
        __print_bar(current_id, i, i + 1, cross_sec, young)
        current_id += 1


def __print_bar(bar_id, id_from, id_to, cross_sec, young):
    print(f'{bar_id}: ({id_from} -> {id_to}) {cross_sec} {young}')


if __name__ == '__main__':
    if len(sys.argv) < 8:
        print('Usage:')
        print(
            '\tgen_baltimore <spans> <span> <height> <section> ' +
            '<young> <Fx> <Fy>'
        )
        sys.exit(1)

    generate_baltimore_structure(
        spans=int(sys.argv[1]),
        span=float(sys.argv[2]),
        height=float(sys.argv[3]),
        cross_sec=float(sys.argv[4]),
        young=float(sys.argv[5]),
        node_load=Vector(
            float(sys.argv[6]),
            float(sys.argv[7])
        )
    )
