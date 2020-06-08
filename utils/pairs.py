def make_round_pairs(sequence):
    """
    Given a sequence [A, B, C] of size n, creates a new sequence
    of the same size where each new item is the pair of the item
    at a given position paired up with next item.
    Additionally, last item is paired with the first one:
    [(A, B), (B, C), (C, A)].

    :param sequence: original sequence
    :return: paired sequence
    """
    length = len(sequence)
    return [
        (sequence[i], sequence[(i + 1) % length])
        for i in range(length)
    ]


def make_pairs(sequence):
    """
    Given a sequence [A, B, C] of size n, creates a new sequence
    of size n - 1 where each element is the pair of the element
    paired up with next item.
    [(A, B), (B, C)].

    :param sequence: original sequence
    :return: paired sequence
    """
    length = len(sequence)
    return [
        (sequence[i], sequence[i + 1])
        for i in range(length - 1)
    ]
