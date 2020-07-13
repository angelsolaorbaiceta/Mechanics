import time


def main_loop(
        update_fn, redraw_fn, should_continue_fn, frame_rate_s=0.03
):
    """
    Starts a main simulation/game loop that will only end when the
    `should_continue_fn` function returns `False`.

    The loop executes every `frame_rate_s` and tries to keep up
    with this rhythm. A message is printed to the console each
    time the loop couldn't be finish on time.

    Inside the loop, first the `update_fn` function is called to
    update the simulated model. Then the `redraw_fn` is called to
    draw the model.

    :param update_fn: function to update the simulated model
    :param redraw_fn: function to redraw the simulated model
    :param should_continue_fn: function to control when the
    simulation has to end
    :param frame_rate_s: number of seconds each frame should take
    :return:
    """
    frame = 1
    time_s = 0
    last_elapsed_s = frame_rate_s

    while should_continue_fn(frame, time_s):
        update_start = time.time()
        update_fn(last_elapsed_s, time_s, frame)
        redraw_fn()
        update_end = time.time()

        elapsed_s = update_end - update_start
        remaining_time_s = frame_rate_s - elapsed_s

        if remaining_time_s > 0:
            time.sleep(remaining_time_s)
            last_elapsed_s = frame_rate_s
        else:
            last_elapsed_s = elapsed_s
            print('Frame took longer than expected!')

        frame += 1
        time_s += last_elapsed_s
