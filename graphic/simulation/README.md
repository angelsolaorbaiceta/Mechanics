# simulation

The _simulation_ package can draw animated vector images to a _tkinter_ canvas.

## Simulation Loop

Inside the [loop.py](./loop.py) module is defined the main algorithm for a simulation time loop.
The simulation loop is responsible for timing the different tasks that take place in a simulation:

1. calls the function that updates the model
2. redraws the graphic representation of the model
3. times the amount of time taken in this process and sleeps for some time in order for the loop to run in equally timed cycles
4. updates the frame count and the total elapsed time
5. checks if the loop should continue; exits otherwise

The `main_loop` function expects four parameters:

- `update_fn`: a function that updates the simulation model
- `redraw_fn`: a function that redraws the model in its current state to the screen
- `should_continue_fn`: a predicate function that determines when the loop should run and when it should be ended
- `frame_rate_s`: the frame rate given in seconds (inverse of the frames per second, defaults to 0.03s)


## Canvas Drawing

In order to draw the simulated model to a _tkinter_ canvas, the `CanvasDrawing` wrapper class is provided. 