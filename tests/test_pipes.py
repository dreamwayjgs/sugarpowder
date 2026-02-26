from sugarpowder.pipes import (
    take, tail, skip,
    where, select,
    dedup, uniq,
    tolist, toset,
    sort, reverse,
)


def test_take():
    result = [1, 2, 3, 4, 5] >> take(3) >> tolist
    assert result == [1, 2, 3]


def test_take_more_than_length():
    result = [1, 2] >> take(10) >> tolist
    assert result == [1, 2]


def test_tail():
    result = [1, 2, 3, 4, 5] >> tail(2) >> tolist
    assert result == [4, 5]


def test_skip():
    result = [1, 2, 3, 4, 5] >> skip(2) >> tolist
    assert result == [3, 4, 5]


def test_where():
    result = [1, 2, 3, 4, 5] >> where(lambda x: x % 2 == 0) >> tolist
    assert result == [2, 4]


def test_select():
    result = [1, 2, 3] >> select(lambda x: x ** 2) >> tolist
    assert result == [1, 4, 9]


def test_chain_where_select():
    result = [1, 2, 3, 4, 5] >> where(lambda x: x % 2 == 0) >> select(lambda x: x ** 2) >> tolist
    assert result == [4, 16]


def test_dedup():
    result = [1, 2, 2, 3, 1, 4] >> dedup >> tolist
    assert result == [1, 2, 3, 4]


def test_uniq():
    result = [1, 1, 2, 2, 3, 1] >> uniq >> tolist
    assert result == [1, 2, 3, 1]


def test_toset():
    result = [1, 2, 2, 3] >> toset
    assert result == {1, 2, 3}


def test_sort():
    result = [3, 1, 2] >> sort >> tolist
    assert result == [1, 2, 3]


def test_sort_reverse():
    result = [3, 1, 2] >> sort(reverse=True) >> tolist
    assert result == [3, 2, 1]


def test_reverse():
    result = [1, 2, 3] >> reverse >> tolist
    assert result == [3, 2, 1]
