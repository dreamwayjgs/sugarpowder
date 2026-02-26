from sugarpowder.pmap import pmap


def add(x, y):
    return x + y


def double(x):
    return x * 2


def test_pmap_two_arrays():
    assert pmap(add, [1, 2, 3], [4, 5, 6]) == [5, 7, 9]


def test_pmap_single_array():
    assert pmap(double, [1, 2, 3]) == [2, 4, 6]


def test_pmap_with_workers():
    assert pmap(add, [1, 2, 3], [4, 5, 6], num_workers=2) == [5, 7, 9]


def test_pmap_empty():
    assert pmap(add, [], []) == []
