from sugarpowder.witherr import witherr, Witherr


@witherr
def div(x: float, y: float) -> float:
    return x / y


@witherr
def strict_int(x) -> int:
    if not isinstance(x, int):
        raise TypeError(f"Expected int, got {type(x)}")
    return x


@Witherr
def div_class(x: float, y: float) -> float:
    return x / y


def test_witherr_success():
    val, err = div(10, 2)
    assert val == 5.0
    assert err is None


def test_witherr_error():
    val, err = div(1, 0)
    assert val is None
    assert isinstance(err, ZeroDivisionError)


def test_witherr_custom_exception():
    val, err = strict_int("hello")
    assert val is None
    assert isinstance(err, TypeError)


def test_Witherr_success():
    val, err = div_class(10, 2)
    assert val == 5.0
    assert err is None


def test_Witherr_error():
    val, err = div_class(1, 0)
    assert val is None
    assert isinstance(err, ZeroDivisionError)
