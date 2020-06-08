from functools import reduce
from tkinter import Canvas

from geom2d import Circle, Polygon, Segment, Rect, AffineTransform


class CanvasDrawing:

    def __init__(self, canvas: Canvas, transform: AffineTransform):
        self.__canvas = canvas
        self.outline_color = '#aa3355'
        self.outline_width = 3
        self.fill_color = ''
        self.transform = transform

    def clear_drawing(self):
        self.__canvas.delete('all')

    def draw_segment(self, segment: Segment):
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
        self.__draw_polygon(
            self.transform.apply_to_circle(circle, divisions)
        )

    def draw_rectangle(self, rect: Rect):
        self.__draw_polygon(
            self.transform.apply_to_rect(rect)
        )

    def draw_polygon(self, polygon: Polygon):
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
