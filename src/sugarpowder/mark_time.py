import time


def mark_time(start_time: float | None = None, prompt="") -> float:
    now = time.time()
    if start_time is not None:
        print(f"Elapsed {prompt}: {now-start_time}")
    print(f"Time Marked: {prompt}")
    return now
