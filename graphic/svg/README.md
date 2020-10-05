# svg

The _svg_ package can draw [SVG](https://developer.mozilla.org/en-US/docs/Web/SVG) images from the geometric primitives defined in the _geom2d_ package.

## Quick Example

To generate the content of an SVG image consisting in a rectangle and a circle:

````python
from geom2d import Point, Size, Circle, Rect
from graphic.svg import primitives, image, attributes

# Geometric primitives
size = Size(200, 200)
circ = Circle(Point(50, 150), 50)
rect = Rect(Point(50, 50), Size(100, 100))

# SVG primitives
blue_fill = attributes.fill_color('#0666D6')
green_fill = attributes.fill_color('#279F43')
prims = (
    primitives.circle(circ, [blue_fill]),
    primitives.rectangle(rect, [green_fill])
)

image.svg_content(size, prims)
````
 which yields the following SVG string:
 
 ````xml
<svg xmlns="http://www.w3.org/2000/svg" version="1.1"
     width="200"
     height="200"
     viewBox="0 0 200 200"
     transform="matrix(1 0 0 1 0 0)">
    <circle cx="50" cy="150" r="50" />
	<rect x="50" y="50" width="100" height="100" />
</svg>
````

Which saved into an `image.svg` would look like:

![](../../img/svg_image_rect_circ.svg)

## Primitives

The _svg_ package, defined in the [primitives.py](./primitives.py) module, currently contains the following primitives:

### `segment`

SVG representation of the `geom2d.Segment` primitive.

```python
from geom2d import Point, Segment
from graphic.svg import attributes, primitives

segment = Segment(Point(10, 15), Point(20, 25))
primitives.segment(segment, [attributes.stroke_width(2)])
```
yields:
```xml
<line x1="10" y1="15" x2="20" y2="25" stroke-width="2"/>
```

### `rectangle`

SVG representation of the `geom2d.Rect` primitive.

```python
from geom2d import Point, Size, Rect
from graphic.svg import attributes, primitives

rect = Rect(Point(10, 15), Size(100, 200))
primitives.rectangle(rect, [attributes.fill_color('blue')])
```
yields:
```xml
<rect x="10" y="15" width="100" height="200" fill="blue"/>
```

### `circle`

SVG representation of the `geom2d.Circle` primitive.

```python
from geom2d import Point, Circle
from graphic.svg import attributes, primitives

circle = Circle(Point(10, 15), 40)
primitives.circle(circle, [attributes.stroke_color('green')])
```
yields:
```xml
<circle cx="10" cy="15" r="40" stroke="green"/>
```

### `polygon`

SVG representation of the `geom2d.Polygon` primitive.

```python
from geom2d import polygons
from graphic.svg import attributes, primitives

polygon = polygons.make_polygon_from_coords((0, 0, 10, 15, 20, 25, 30, 35))
primitives.polygon(polygon, [attributes.stroke_width(1)])

```
yields:
```xml
<polygon points="0,0 10,15 20,25 30,35" stroke-width="1"/>
```

### `polyline`

SVG representation of a list of points connected to form an open line.

```python
from geom2d import Point
from graphic.svg import attributes, primitives

points = (Point(0, 0), Point(10, 15), Point(20, 25))
primitives.polyline(points, [attributes.stroke_color('red')])
```
yields:
```xml
<polyline points="0,0 10,15 20,25" stroke="red"/>
```

### `text`

```python

```
yields:
```xml

```

### `group`

```python

```
yields:
```xml

```

### `arrow`

```python

```
yields:
```xml

```


## Attributes

To style the primitives, defined in the [attributes.py](./attributes.py) module are the current available attributes:

- `stroke_color`
- `stroke_width`
- `fill_color`
- `fill_opacity`
- `affine_transform`
- `font_size`
- `font_family` 