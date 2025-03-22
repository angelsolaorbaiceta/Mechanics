from geom2d.circle import Circle
from geom2d.nums import are_close_enough, value_or_zero
from geom2d.point import Point
from geom2d.polygon import Polygon
from geom2d.rect import Rect
from geom2d.segment import Segment


class AffineTransform:
    """
    An affine transformation is equivalent to a linear
    transformation plus a translation.
    An affine transformation can be defined using matrix notation:

    `⎡ sx  shx tx ⎤`\n
    `⎪ shy sy  ty ⎪`\n
    `⎣ 0   0   1  ⎦`\n

    Affine transformations have the following terms:

    - `sx`: scale in the x-direction
    - `sy`: scale in the y-direction
    - `tx`: translation in the x-direction
    - `ty`: translation in the y-direction
    - `shx`: shear in the x-direction
    - `shy`: shear in the y-direction
    """

    def __init__(self, sx=1, sy=1, tx=0, ty=0, shx=0, shy=0):
        self.sx = value_or_zero(sx)
        self.sy = value_or_zero(sy)
        self.tx = value_or_zero(tx)
        self.ty = value_or_zero(ty)
        self.shx = value_or_zero(shx)
        self.shy = value_or_zero(shy)

    def apply_to_point(self, point: Point):
        """
        Computes a new `Point` result of applying this affine
        transformation to the given `point`.

        :param point: source `Point`
        :return: transformed `Point`
        """
        return Point(
            (self.sx * point.x) + (self.shx * point.y) + self.tx,
            (self.shy * point.x) + (self.sy * point.y) + self.ty,
        )

    def apply_to_segment(self, segment: Segment):
        """
        Computes a new `Segment` result of applying this affine
        transformation to the given `segment`.

        :param segment: source `Segment`
        :return: transformed `Segment`
        """
        return Segment(
            self.apply_to_point(segment.start), self.apply_to_point(segment.end)
        )

    def apply_to_polygon(self, polygon: Polygon):
        """
        Computes a new `Polygon` result of applying this affine
        transformation to the given `Polygon`.

        :param polygon: source `Polygon`
        :return: transformed `Polygon`
        """
        return Polygon([self.apply_to_point(v) for v in polygon.vertices])

    def apply_to_rect(self, rect: Rect):
        """
        Computes a `Polygon` result of applying this affine
        transformation to the given `Rect`.

        After applying a generic affine transformation to a
        rectangle, this may not be a rectangle whose sides are
        aligned with the horizontal and vertical directions
        anymore, therefore, this method returns a `Polygon` and
        not a `Rect`.

        :param rect: source `Rect`
        :return: transformed `Polygon`
        """
        return self.apply_to_polygon(rect.to_polygon())

    def apply_to_circle(self, circle: Circle, divisions=30):
        """
        Computes a `Polygon` result of applying this affine
        transformation to the given `Circle`.

        After applying a generic affine transformation to a circle,
        this may not be a circle anymore. A shear transformation,
        for instance, would turn the circle into some kind of
        ellipse.
        For this reason, this method returns a `Polygon` and not
        a `Circle`.

        :param circle: source `Circle`
        :param divisions: point count used to turn the circle into
        a polygon prior to the transformation
        :return: transformed `Polygon`
        """
        return self.apply_to_polygon(circle.to_polygon(divisions))

    def then(self, other):
        """
        Computes a new transformation result of concatenating
        another transformation `other` with the current one.

        The resulting transformation's effect is equal to applying
        this transformation then `other` in sequence.

        :param other: `AffineTransform` to be applied after this
        :return: combined `AffineTransform`
        """
        return AffineTransform(
            sx=other.sx * self.sx + other.shx * self.shy,
            sy=other.shy * self.shx + other.sy * self.sy,
            tx=other.sx * self.tx + other.shx * self.ty + other.tx,
            ty=other.shy * self.tx + other.sy * self.ty + other.ty,
            shx=other.sx * self.shx + other.shx * self.sy,
            shy=other.shy * self.sx + other.sy * self.shy,
        )

    def inverse(self):
        """
        Computes this affine transformation's inverse.

        The inverse transformation [J] of a transformation [T] is
        such that [T][J] = [I], where [I] is the identity.

        :return: inverse `AffineTransform`
        """
        denom = self.sx * self.sy - self.shx * self.shy
        return AffineTransform(
            sx=self.sy / denom,
            sy=self.sx / denom,
            tx=(self.ty * self.shx - self.sy * self.tx) / denom,
            ty=(self.tx * self.shy - self.sx * self.ty) / denom,
            shx=-self.shx / denom,
            shy=-self.shy / denom,
        )

    def __eq__(self, other):
        """
        Two affine transformations are equal if all its values are
        equal: sx, sy, shx, shy, tx and ty.

        :param other: `AffineTransform`
        :return: are the affine transformations equal?
        """
        if self is other:
            return True

        if not isinstance(other, AffineTransform):
            return False

        return (
            are_close_enough(self.sx, other.sx)
            and are_close_enough(self.sy, other.sy)
            and are_close_enough(self.tx, other.tx)
            and are_close_enough(self.ty, other.ty)
            and are_close_enough(self.shx, other.shx)
            and are_close_enough(self.shy, other.shy)
        )

    def __str__(self):
        return (
            f"(sx: {self.sx}, sy: {self.sy}, "
            + f"shx: {self.shx}, shy: {self.shy}, "
            + f"tx: {self.tx}, ty: {self.ty})"
        )
