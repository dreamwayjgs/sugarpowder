from functools import update_wrapper, wraps
from typing import Callable, Generic, ParamSpec, TypeVar


T = TypeVar("T")
P = ParamSpec("P")


class Witherr(Generic[P, T]):
    """
    Go style error handling - Class Wrapper version
    """

    def __init__(self, func: Callable[P, T]):
        self.func = func
        update_wrapper(self, func)

    def __call__(
        self, *args: P.args, **kwargs: P.kwargs
    ) -> tuple[T, None] | tuple[None, Exception]:
        try:
            return self.func(*args, **kwargs), None
        except Exception as err:
            return None, err


# Function Wrapper version
def witherr(
    f: Callable[P, T]
) -> Callable[..., tuple[T, None] | tuple[None, Exception]]:
    """
    Go style error handling - Function Wrapper version
    """

    @wraps(f)
    def wrapper(
        *args: P.args, **kwargs: P.kwargs
    ) -> tuple[T, None] | tuple[None, Exception]:
        try:
            return f(*args, **kwargs), None
        except Exception as err:
            return None, err

    return wrapper
