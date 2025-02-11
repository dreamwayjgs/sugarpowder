from functools import partial
from typing import Any, Type, Callable


class Infix:
    def __init__(self, function: Callable[..., bool]):
        self.function = function

    def __ror__(self, other: Any) -> "Infix":
        return Infix(partial(self.function, other))

    def __or__(self, other: Any) -> bool:
        return self.function(other)


def is_instance(obj: Any, cls: Type) -> bool:
    return isinstance(obj, cls)


# 사용 예제
# result: bool = 3 | isa | int
# print(result)  # 출력: True
# result = 3 | isa | str
# print(result)  # 출력: False
# result = "hello" | isa | str
# print(result)  # 출력: True
isa = Infix(is_instance)
