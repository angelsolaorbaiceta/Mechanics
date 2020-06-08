import sys

from geom2d import Vector


def generate_warren_structure(
        spans: int,
        span: float, height: float,
        cross_sec: float, young: float,
        node_load: Vector
):
    if spans % 2 != 0:
        raise ValueError('Need an even number of spans')

    print(f'# Warren truss with {spans} spans\n')

    __generate_nodes(spans, span, height)
    __generate_loads(spans, node_load)
    __generate_bars(spans, cross_sec, young)


def __generate_nodes(spans: int, span: float, height: float):
    print('nodes')

    __gen_lower_nodes(spans, span)
    __gen_upper_nodes(spans, span, height)


def __gen_lower_nodes(spans: int, span: float):
    print('# lower nodes')

    x = 0.0
    for i in range(spans + 1):
        node = f'{i + 1}: ({x}, 0.0) '

        if i == 0:
            node += '(xy)'
        elif i == spans:
            node += '(y)'
        else:
            node += '()'

        print(node)
        x += span


def __gen_upper_nodes(spans: int, span: float, height: float):
    print('# upper nodes')

    x = span
    for i in range(spans + 1, 2 * spans):
        print(f'{i + 1}: ({x}, {height}) ()')
        x += span


def __generate_loads(spans: int, node_load: Vector):
    print('\nloads')

    nodes_count = 2 * spans
    for i in range(nodes_count):
        print(f'{i + 1} -> ({node_load.u}, {node_load.v})')


def __generate_bars(spans: int, cross_sec: float, young: float):
    print('\nbars')

    __gen_horizontal_bars(spans, cross_sec, young)
    __gen_vertical_bars(spans, cross_sec, young)
    __gen_diagonal_bars(spans, cross_sec, young)


def __gen_horizontal_bars(
        spans: int,
        cross_sec: float,
        young: float
):
    print('# horizontal bars')

    for i in range(spans):
        __print_bar(i + 1, i + 1, i + 2, cross_sec, young)

    for i in range(spans + 1, 2 * spans - 1):
        __print_bar(i, i + 1, i + 2, cross_sec, young)


def __gen_vertical_bars(
        spans: int,
        cross_sec: float,
        young: float
):
    print('# vertical bars')

    start_id = 2 * spans - 1
    node_ids = range(2, spans + 1)

    for i, id_from in enumerate(node_ids):
        __print_bar(
            i + start_id,
            id_from,
            id_from + spans,
            cross_sec,
            young
        )


def __gen_diagonal_bars(
        spans: int,
        cross_sec: float,
        young: float
):
    print('# diagonal bars')

    start_id = 3 * spans - 2
    id_from = 1
    id_to = spans + 2

    for i in range(spans):
        __print_bar(start_id + i, id_from, id_to, cross_sec, young)

        next_id_to = id_from + 2
        id_from = id_to
        id_to = next_id_to


def __print_bar(bar_id, id_from, id_to, cross_sec, young):
    print(f'{bar_id}: ({id_from} -> {id_to}) {cross_sec} {young}')


if __name__ == '__main__':
    if len(sys.argv) < 8:
        print('Usage:')
        print(
            '\tgen_warren <spans> <span> <height> <section> ' +
            '<young> <Fx> <Fy>'
        )
        sys.exit(1)

    generate_warren_structure(
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
