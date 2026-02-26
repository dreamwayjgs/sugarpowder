from dataclasses import dataclass
from datetime import datetime
from typing import Any

import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

from sugarpowder.serialization import (
    blosc_dill,
    blosc_pickle,
    blosc_undill,
    blosc_unpickle,
)


@dataclass
class SampleData:
    num: int
    nums: list[int]
    dct: dict[str, Any]

    def __eq__(self, other):
        return self.num == other.num and self.nums == other.nums and self.dct == other.dct


def sample_df():
    return pd.DataFrame({
        "X": [1, 2, 3],
        "Y": ["a", "b", "c"],
        "Z": [datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3)],
    })


def test_blosc_pickle_dataframe():
    df = sample_df()
    restored = blosc_unpickle(blosc_pickle(df))
    assert_frame_equal(df, restored)


def test_blosc_pickle_object():
    obj = SampleData(1, [1, 2, 3], {"a": "b"})
    restored = blosc_unpickle(blosc_pickle(obj))
    assert obj == restored


def test_blosc_dill_dataframe():
    df = sample_df()
    restored = blosc_undill(blosc_dill(df))
    assert_frame_equal(df, restored)


def test_blosc_dill_lambda():
    fn = lambda x: x * 2
    restored = blosc_undill(blosc_dill(fn))
    assert restored(3) == 6


def test_blosc_unpickle_raises_without_args():
    with pytest.raises(Exception):
        blosc_unpickle()
