from sugarpowder.lists import dedup, deep_flatten


def test_dedup_primitives():
    assert dedup([3, 1, 2, 1, 3]) == [3, 1, 2]


def test_dedup_preserves_order():
    assert dedup([3, 1, 2, 1, 3]) == [3, 1, 2]


def test_dedup_with_key():
    items = [{"id": 1, "name": "a"}, {"id": 1, "name": "b"}, {"id": 2, "name": "c"}]
    assert dedup(items, key=lambda x: x["id"]) == [{"id": 1, "name": "a"}, {"id": 2, "name": "c"}]


def test_dedup_unhashable():
    assert dedup([[1, 2], [3, 4], [1, 2]]) == [[1, 2], [3, 4]]


def test_deep_flatten():
    assert deep_flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert deep_flatten([[1, [2, 3]], [4]]) == [1, 2, 3, 4]
    assert deep_flatten([1, [2, [3, [4]]]]) == [1, 2, 3, 4]
    assert deep_flatten(["ab", ["cd"]]) == ["ab", "cd"]
    assert deep_flatten([]) == []
