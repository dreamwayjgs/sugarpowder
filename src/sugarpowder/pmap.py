from multiprocessing import Pool
from typing import Callable, Iterable, List, TypeVar

T = TypeVar("T")
R = TypeVar("R")


def pmap(
    func: Callable[..., R],
    *arrays: Iterable[T],
    num_workers: int | None = None,
) -> List[R]:
    """
    Parallel zip-based map for element-wise operations across multiple iterables.
    Equivalent to list(map(func, *arrays)) but executed in parallel via multiprocessing.

    - func: The function to apply element-wise
    - arrays: One or more iterables
    - num_workers: Number of worker processes (None = CPU count)
    """
    data = list(zip(*arrays))
    with Pool(processes=num_workers) as pool:
        return pool.starmap(func, data)
