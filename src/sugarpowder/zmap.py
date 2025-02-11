from multiprocessing import Pool
from typing import Callable, Iterable, List, TypeVar

T = TypeVar("T")  # 입력 데이터 타입
R = TypeVar("R")  # 결과 데이터 타입


def zmap_parallel(
    func: Callable[..., R], *arrays: Iterable[T], num_workers: int | None = None
) -> List[R]:
    """
    zmap_parallel: Parallel zip-based map for element-wise operations
    - func: The function to apply element-wise
    - arrays: One or more iterables to broadcast
    - num_workers: Number of processes for multiprocessing
    - Returns: A list of results, with the function applied in parallel
    """
    data = list(zip(*arrays))
    with Pool(processes=num_workers) as pool:
        return pool.starmap(func, data)


def zmap(
    func: Callable[..., R],
    *arrays: Iterable[T],
    use_parallel: bool = False,
    num_workers: int | None = None,
) -> List[R]:
    """
    zmap: Zip-based map for element-wise operations
    - func: The function to apply element-wise
    - arrays: One or more iterables to broadcast
    - Returns: A list of results, with the function applied to corresponding elements
    """
    if use_parallel:
        return zmap_parallel(func, *arrays, num_workers=num_workers)
    return [func(*args) for args in zip(*arrays)]
