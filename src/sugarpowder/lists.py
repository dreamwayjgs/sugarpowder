from typing import Callable, Iterable, TypeVar

T = TypeVar("T")


def dedup(seq: Iterable[T], key: Callable[[T], object] | None = None) -> list[T]:
    """Deduplicate while preserving order.

    key: optional function to extract comparison key from each element.
         Useful for unhashable types like dicts.
    """
    items = list(seq)

    if key is not None:
        seen_keys: list = []
        result = []
        for item in items:
            k = key(item)
            if k not in seen_keys:
                seen_keys.append(k)
                result.append(item)
        return result

    try:
        return list(dict.fromkeys(items))
    except TypeError:
        # unhashable elements - fall back to O(n²) equality check
        seen: list = []
        result = []
        for item in items:
            if item not in seen:
                seen.append(item)
                result.append(item)
        return result


def deep_flatten(iterable: Iterable) -> list:
    result = []
    for item in iterable:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            result.extend(deep_flatten(item))
        else:
            result.append(item)
    return result
