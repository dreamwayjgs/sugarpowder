from dataclasses import dataclass
from typing import Any
from sugarpowder.serialization import (
    blosc_pickle,
    blosc_unpickle,
    df_to_hex,
    df_to_parquetstream,
    hex_to_df,
    parquetstream_to_df,
)
from sugarpowder.utils import create_directory_recursive
from sugarpowder.witherr import witherr, Witherr
from sugarpowder.pipes import take, select, where, tolist, tail
from sugarpowder.mark_time import mark_time

# from sugarpowder.utils import df_to_hex, df_to_parquetstream, hex_to_df, parquetstream_to_df
from datetime import datetime
import pandas as pd
from pandas.testing import assert_frame_equal

from sugarpowder.zmap import zmap


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

    dfhex = df_to_hex(df)
    hexdf = hex_to_df(dfhex)

    try:
        assert_frame_equal(df, ndf)
        assert_frame_equal(df, hexdf)
    except:
        assert False, "Frame Equal Failed"


def test_blosc_pickle():
    X = [1, 2, 3, 4]
    Y = ["a", "b", "c", "d"]
    Z = [datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3), datetime(2020, 1, 4)]

    df = pd.DataFrame({"X": X, "Y": Y, "Z": Z})
    df_pickled = blosc_pickle(df)
    newdf = blosc_unpickle(df_pickled)

    try:
        assert_frame_equal(df, newdf)
    except:
        assert False, "Frame Not Equal"


def test_create_directory_recursive():
    create_directory_recursive("res/test")


def add(x, y):
    return x + y


def test_zmap():

    # 테스트 데이터
    x = [1, 2, 3]
    y = [4, 5, 6]

    # 싱글 프로세스 실행
    assert zmap(add, x, y) == [5, 7, 9]
    assert zmap(lambda x, y: x + y, x, y) == [5, 7, 9]

    # 멀티프로세스 실행
    assert zmap(add, x, y, use_parallel=True, num_workers=2) == [5, 7, 9]


@dataclass
class MyClass:
    num: int
    nums: list[int]
    dct: dict[str, Any]
    dcts: list[dict[str, Any]]

    def __eq__(self, other):
        return (
            self.num == other.num
            and self.nums == other.nums
            and self.dct == other.dct
            and self.dcts == other.dcts
        )


def test_dill():
    X = [1, 2, 3, 4]
    Y = ["a", "b", "c", "d"]
    Z = [datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3), datetime(2020, 1, 4)]

    df = pd.DataFrame({"X": X, "Y": Y, "Z": Z})
    df_pickled = blosc_pickle(df)
    newdf = blosc_unpickle(df_pickled)

    try:
        assert_frame_equal(df, newdf)
    except:
        assert False, "Frame Not Equal"

    A = MyClass(1, [1, 2], {"a": "b"}, [{"c": "d"}, {"e": "f"}])
    B = MyClass(1, [1, 3], {"a": "b"}, [{"c": "d"}, {"e": "f"}])
    C = MyClass(1, [1, 2], {"a": "b"}, [{"c": "d"}, {"e": "f"}])

    assert A != B
    assert A == C
    assert B != C


if __name__ == "__main__":
    print("Run Tests")
    s = mark_time()
    test_pipes()
    mark_time(s, "Test pipes")
