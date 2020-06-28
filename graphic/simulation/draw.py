from functools import reduce
from tkinter import Canvas

from geom2d import Circle, Polygon, Segment, Rect, AffineTransform


class CanvasDrawing:
    """
    Wraps a tkinter `Canvas` and provides methods to draw on it.

    `CanvasDrawing` includes an affine transformation associated
    with the drawing: all drawing commands will use the
    transformation before forwarding the drawing to the canvas.
    """

    def __init__(self, canvas: Canvas, transform: AffineTransform):
        self.__canvas = canvas
        self.outline_color = '#aa3355'
        self.outline_width = 3
        self.fill_color = ''
        self.transform = transform

    def clear_drawing(self):
        """
        Clears the drawing setting it blank.
        """
        self.__canvas.delete('all')

    def draw_segment(self, segment: Segment):
        """
        Draws the segment to the canvas after applying it the
        drawing's transformation.

        :param segment: `Segment`
        """
        segment_t = self.transform.apply_to_segment(segment)
        self.__canvas.create_line(
            segment_t.start.x,
            segment_t.start.y,
            segment_t.end.x,
            segment_t.end.y,
            fill=self.outline_color,
            width=self.outline_width
        )

    def draw_circle(self, circle: Circle, divisions=30):
        """
        Draws the circle to the canvas after applying it the
        drawing's transformation.

        The number of divisions is used to transform the circle
        into a generic polygon prior to the transformation
        application.

        :param circle: `Circle`
        :param divisions: `int` defaulting to 30
        """
        self.__draw_polygon(
            self.transform.apply_to_circle(circle, divisions)
        )

    def draw_rectangle(self, rect: Rect):
        """
        Draws the rectangle to the canvas after applying it the
        drawing's transformation.

        :param rect: `Rect`
        """
        self.__draw_polygon(
            self.transform.apply_to_rect(rect)
        )

    def draw_polygon(self, polygon: Polygon):
        """
        Draws the polygon to the canvas after applying it the
        drawing's transformation.

        :param polygon: `Polygon`
        """
        self.__draw_polygon(
            self.transform.apply_to_polygon(polygon)
        )

    def __draw_polygon(self, polygon: Polygon):
        vertices = reduce(
            list.__add__,
            [[v.x, v.y] for v in polygon.vertices]
        )

        self.__canvas.create_polygon(
            vertices,
            fill=self.fill_color,
            outline=self.outline_color,
            width=self.outline_width
        )

    def draw_arrow(self, segment: Segment, length, height):
        """
        Draws a segment with an arrow in it's end.
        The arrow's dimensions are given by `length` and `height`.

        :param segment: `Segment`
        :param length: `Int` length of the arrow head
        :param height: `Int` height of the arrow head
        """
        director = segment.direction_vector()
        v_l = director.opposite().with_length(length)
        v_h1 = director.perpendicular().with_length(height / 2.0)
        v_h2 = v_h1.opposite()

        self.draw_segment(segment)
        self.draw_segment(
            Segment(
                segment.end,
                segment.end.displaced(v_l + v_h1)
            )
        )
        self.draw_segment(
            Segment(
                segment.end,
                segment.end.displaced(v_l + v_h2)
            )
        )
