from sugarpowder.witherr import witherr, Witherr
from sugarpowder.pipes import take, select, where, tolist, tail
from sugarpowder.mark_time import mark_time


@witherr
def div1(x: float, y: float) -> float:
    """
    test function - divide
    """
    return x / y


@Witherr
def div2(x: float, y: float) -> float:
    """
    test function - divide
    """
    return x / y


def test_witherr():
    val, err = div1(1, 1)
    assert err is None

    val, err = div1(1, 0)
    assert isinstance(err, ZeroDivisionError)


def test_Witherr():
    val, err = div2(1, 1)
    assert err is None

    val, err = div2(1, 0)
    assert isinstance(err, ZeroDivisionError)


def test_pipes():
    arr = [1, 2, 3, 4, 5]
    arr_first2 = arr >> take(2) >> tolist
    assert arr_first2 == [1, 2]

    arr_last2 = arr >> tail(2) >> tolist
    assert arr_last2 == [4, 5]

    # arr_powered = filter(lambda x: x % 2 == 0, arr)
    # arr_powered = list(map(lambda x: x**2, arr_powered))

    arr_powered = arr >> where(lambda x: x % 2 == 0) >> select(lambda x: x**2) >> tolist
    assert arr_powered == [4, 16]


if __name__ == "__main__":
    print("Run Tests")
    s = mark_time()
    test_pipes()
    mark_time(s, "Test pipes")
