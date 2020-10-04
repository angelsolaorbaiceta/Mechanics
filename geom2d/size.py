from geom2d.nums import are_close_enough


class Size:
    """
    Size is a tuple of a width and a height.
    It represents the dimensions of a rectangle.
    """

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def scaled(self, scale: float):
        """
        Creates a scaled version of the size using the given scale.

        :param scale: `float`
        :return: scaled `Size`
        """
        return Size(
            self.width * scale,
            self.height * scale
        )

    def __eq__(self, other):
        """
        Two sizes are equal if their widths and heights are equal.

        :param other: `Size`
        :return: are the sizes equal?
        """
        if self is other:
            return True

        if not isinstance(other, Size):
            return False

        return are_close_enough(self.width, other.width) \
               and are_close_enough(self.height, other.height)
