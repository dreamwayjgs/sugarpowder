from sugarpowder.zmap import zmap


def add(x, y):
    return x + y


def test_zmap_single_array():
    result = zmap(lambda x: x * 2, [1, 2, 3])
    assert result == [2, 4, 6]


def test_zmap_two_arrays():
    result = zmap(add, [1, 2, 3], [4, 5, 6])
    assert result == [5, 7, 9]


def test_zmap_lambda():
    result = zmap(lambda x, y: x + y, [1, 2, 3], [4, 5, 6])
    assert result == [5, 7, 9]


def test_zmap_parallel():
    result = zmap(add, [1, 2, 3], [4, 5, 6], use_parallel=True, num_workers=2)
    assert result == [5, 7, 9]


def test_zmap_empty():
    result = zmap(add, [], [])
    assert result == []
