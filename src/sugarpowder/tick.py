import inspect
import time


def tick(since: float | None = None, label: str = "", msg: str = "") -> float:
    now = time.perf_counter()
    if since is not None:
        frame = inspect.currentframe()
        assert frame is not None
        caller = frame.f_back
        assert caller is not None
        location = f"[{caller.f_code.co_name}:{caller.f_lineno}] "

        elapsed_label = f" {label}" if label else ""
        suffix = f" / {msg}" if msg else ""
        print(f"{location}Elapsed{elapsed_label}: {now - since:.4f}s{suffix}")

    return now
