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
prims = [
    primitives.circle(circ, [blue_fill]),
    primitives.rectangle(rect, [green_fill])
]

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

- `segment`
- `rectangle`
- `circle`
- `polygon`
- `polyline`
- `text`
- `group`
- `arrow`

## Attributes

To style the primitives, defined in the [attributes.py](./attributes.py) module are the current available attributes:

- `stroke_color`
- `stroke_width`
- `fill_color`
- `fill_opacity`
- `affine_transform`
- `font_size`
- `font_family` 