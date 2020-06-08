from tkinter import Tk, Canvas

from geom2d import Point, Circle, AffineTransform
from graphic.simulation.draw import CanvasDrawing
from graphic.simulation.loop import main_loop

tk = Tk()
tk.title("Hello Motion")

canvas = Canvas(tk, width=600, height=600)
canvas.grid(row=0, column=0)

max_frames = 100

transform = AffineTransform(
    sx=1, sy=-1, tx=150, ty=600, shx=-0.5, shy=0
)
drawing = CanvasDrawing(canvas, transform)
circle = Circle(Point(300, 300), 0)


def update_system(time_delta_s, time_s, frame):
    circle.radius = (circle.radius + 15) % 450
    tk.update()


def redraw():
    drawing.clear_drawing()
    drawing.draw_circle(circle, 50)


def should_continue(frame, time_s):
    return frame <= max_frames


main_loop(update_system, redraw, should_continue)
tk.mainloop()
