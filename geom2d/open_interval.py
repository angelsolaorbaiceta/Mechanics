from .nums import are_close_enough


class OpenInterval:
    """
    An open interval is one where both ends aren't included.

    For example, the range (2, 7) includes every number between
    its two ends, 2 and 7, but the ends are excluded.
    """

    def __init__(self, start, end):
        if start > end:
            raise ValueError('start should be smaller than end')
        self.start = start
        self.end = end

    @property
    def length(self):
        """
        Length of the interval: end - start.

        :return: length
        """
        return self.end - self.start

    def contains(self, value: float):
        """
        Tests whether this interval contains a given value or not.

        :param value: `float` number
        :return: is the value contained in the interval?
        """
        return self.start < value < self.end

    def overlaps_interval(self, other):
        """
        Tests whether this and other interval overlap.

        :param other: `OpenInterval`
        :return: `bool` do intervals overlap?
        """
        if are_close_enough(self.start, other.start) and \
                are_close_enough(self.end, other.end):
            return True

        return self.contains(other.start) \
               or self.contains(other.end) \
               or other.contains(self.start) \
               or other.contains(self.end)

    def compute_overlap_with(self, other):
        """
        Given two overlapping ranges, computes the range of their
        overlap.

        If the ranges don't overlap, `None` is returned.
        :param other: `OpenRange`
        :return: ranges overlap
        """
        if not self.overlaps_interval(other):
            return None

        return OpenInterval(
            max(self.start, other.start),
            min(self.end, other.end)
        )
