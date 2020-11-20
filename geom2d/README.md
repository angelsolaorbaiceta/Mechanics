# geom2d

The _geom2d_ package implements 2D geometry primitives and operations.

__Contents__:

- [Primitives](#primitives)
- [Transformations](#transformations)
- [Intersections](#intersections)

## Primitives

This _geom2d_ package defines the following two-dimensional geometric primitives:

- `Point`: a position in the plane defined by its coordinates `x`and `y`.
- `Vector`: a direction in the plane defined by its projections `u` and `v`.
- `Segment`: a straight line segment defined between two points: `start`and `end`. The middle points of a segment can be iterated using a parameter `t` which varies from 0 to 1.
- `Line`: an infinite straight line defined by a base point `base` and a direction vector `direction`.
- `Size`: defined by a `width` and `length`.
- `Rect`: a rectangle defined by an origin point `origin` and a `Size`.
- `Circle`: defined by a center point `center` and a `radius`.
- `Polygon`: defined by a sequence of ordered `vertices` (instances of the `Point` class).

## Transformations

Apart from these primitives, there's an important algebraic concept defined in this package: `AffineTransform`.
The `AffineTransform` class defined in the [affine_transf.py](./affine_transf.py) module represents an affine transformation.
This class can be used to apply this type of transformations to the geometric primitives.

To create an affine transformation, use the constructor:

```python
from geom2d import AffineTransform

transf = AffineTransform(sx=1, sy=2, tx=10, ty=20, shx=0.5, shy=0.75)
```

where the terms correspond to:

- `sx`: scale in the x-axis
- `sy`: scale in the y-axis
- `tx`: translation along the x-axis
- `ty`: translation along the y-axis
- `shx`: shear in the x-axis
- `shy`: shear in the y-axis

You may also create certain types of affine transformations using the factory functions in the [affine_transforms.py](./affine_transforms.py) module:

- `make_scale(sx, sy, center)`: creates a scale transformation with `sx` and `sy` factors and using `center` as reference
- `make_rotation(radians, center)`: creates a rotation transformation of `radians` about the `center` point 


Affine transformations can be applied to almost every primitive in the _geom2d_ package:

- `apply_to_point(point)`
- `apply_to_segment(segment)`
- `apply_to_polygon(polygon)`
- `apply_to_rect(rect)`: returns the transformed `Rect` as a `Polygon`
- `apply_to_circle(circ)`: returns the transformed `Circle` as a `Polygon`

Affine transformations can be concatenated using the `then(other)` method:

```python
import math
from geom2d import make_scale, make_rotation, Point

center = Point(10, 20)
scale = make_scale(2, 4, center)
rotate = make_rotation(math.pi, center)

scale_and_rotate = scale.then(rotate)
```

In this case, applying the `scale_and_rotate` affine transformation is equivalent to first applying the `scale` transformation, then `rotate`.


## Intersections 

There are algorithms defined to compute intersections between:

- two `Segment` instances:

```python
from geom2d import Segment, Point

segment_one = Segment(Point(0, 0), Point(100, 100))
segment_two = Segment(Point(0, 100), Point(100, 0))

segment_one.intersection_with(segment_two)
```

yields:
> `{ x: 50, y: 50 }`

- two `Line` instances:

```python
from geom2d import Line, Point, Vector

line_one = Line(Point(0, 0), Vector(1, 1))
line_two = Line(Point(0, 100), Vector(1, -1))

line_one.intersection_with(line_two)
```

also yields:
> `{ x: 50, y: 50 }`

- two `Rect` instances:

```python
from geom2d import Rect, Point, Size

rect_one = Rect(Point(0, 0), Size(50, 50))
rect_two = Rect(Point(10, 10), Size(100, 100))
rect_one.intersection_with(rect_two)
```

yields the rectangle:
> `{ origin: { x: 10, y: 10 }, size: { width: 40, height: 40 } }`

We can also compute the overlap between two circles in form a penetration vector:

```python
from geom2d import Circle, Point

circ_one = Circle(Point(0, 0), 20)
circ_two = Circle(Point(10, 10), 30)
circ_one.penetration_vector(circ_two)
```
which yields the vector:
> `{ u: -25.355339059327374, v: -25.355339059327374 }`