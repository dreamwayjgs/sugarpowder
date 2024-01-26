from sugarpowder.witherr import witherr, Witherr
from sugarpowder.pipes import take, select, where, tolist, tail
from sugarpowder.mark_time import mark_time
from sugarpowder.utils import df_to_parquetstream, parquetstream_to_df
from datetime import datetime
import pandas as pd
from pandas.testing import assert_frame_equal


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


def test_df_parquetstream():
    X = [1, 2, 3, 4]
    Y = ["a", "b", "c", "d"]
    Z = [datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3), datetime(2020, 1, 4)]

    df = pd.DataFrame({"X": X, "Y": Y, "Z": Z})
    pq = df_to_parquetstream(df)
    ndf = parquetstream_to_df(pq)

    try:
        assert_frame_equal(df, ndf)
        assert True
    except:
        assert False, "Frame Eqaul Failed"


if __name__ == "__main__":
    print("Run Tests")
    s = mark_time()
    test_pipes()
    mark_time(s, "Test pipes")
