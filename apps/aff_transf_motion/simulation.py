from tkinter import Tk, Canvas, Button

from geom2d import affine_transforms as tf, Segment, Point
from graphic.simulation import CanvasDrawing, main_loop


def simulate(transform, primitives, config):
    # ---------- UI DEFINITION ---------- #
    tk = Tk()
    tk.title("Affine Transformations")
    tk.minsize(width=400, height=400)

    canvas = Canvas(tk)
    canvas.pack(fill='both', side='top', expand=True)

    def start_simulation():
        tk.update()
        main_loop(update_system, redraw, should_continue)

    button = Button(tk, text='Play', command=start_simulation)
    button.pack(anchor='center', side='bottom')

    # ---------- UPDATE, DRAW & CONTINUE ---------- #
    frames = config['frames']
    transform_seq = __make_transform_sequence(transform, frames)
    axis_length = config['axes']['length']
    x_axis = Segment(Point(0, 0), Point(axis_length, 0))
    y_axis = Segment(Point(0, 0), Point(0, axis_length))
    drawing = CanvasDrawing(canvas, transform_seq[0])

    def update_system(time_delta_s, time_s, frame):
        drawing.transform = transform_seq[frame - 1]
        tk.update()

    def redraw():
        drawing.clear_drawing()

        drawing.outline_width = config['axes']['stroke-width']
        drawing.outline_color = config['axes']['x-color']
        drawing.draw_arrow(
            x_axis,
            config['axes']['arrow-length'],
            config['axes']['arrow-height']
        )

        drawing.outline_color = config['axes']['y-color']
        drawing.draw_arrow(
            y_axis,
            config['axes']['arrow-length'],
            config['axes']['arrow-height']
        )

        drawing.outline_width = config['geometry']['stroke-width']
        drawing.outline_color = config['geometry']['stroke-color']

        for circle in primitives['circs']:
            drawing.draw_circle(circle)

        for rect in primitives['rects']:
            drawing.draw_rectangle(rect)

        for polygon in primitives['polys']:
            drawing.draw_polygon(polygon)

        for segment in primitives['segs']:
            drawing.draw_segment(segment)

    def should_continue(frame, time_s):
        return frame <= frames

    # ---------- MAIN LOOP ---------- #
    redraw()
    tk.mainloop()


def __make_transform_sequence(end_transform, frames):
    start_transform = tf.AffineTransform(sx=1, sy=1, tx=20, ty=20)
    return tf.ease_in_out_interpolation(
        start_transform, end_transform, frames
    )
