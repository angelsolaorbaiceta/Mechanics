import time


def main_loop(
        update_fn, redraw_fn, should_continue_fn, frame_rate_s=0.03
):
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
            print(f'Frame took longer than expected!')

        frame += 1
        time_s += last_elapsed_s

