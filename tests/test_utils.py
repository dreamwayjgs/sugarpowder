import tempfile
from datetime import datetime
from pathlib import Path

import pandas as pd
from pandas.testing import assert_frame_equal

from sugarpowder.serialization import (
    base64_to_df,
    df_to_base64,
    df_to_hex,
    df_to_parquetstream,
    hex_to_df,
    parquetstream_to_df,
)
from sugarpowder.lists import dedup, deep_flatten
from sugarpowder.strings import fix_mac_hangul
from sugarpowder.fs import create_directory_recursive


def sample_df():
    return pd.DataFrame({
        "X": [1, 2, 3],
        "Y": ["a", "b", "c"],
        "Z": [datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3)],
    })


def test_parquetstream_roundtrip():
    df = sample_df()
    assert_frame_equal(df, parquetstream_to_df(df_to_parquetstream(df)))


def test_hex_roundtrip():
    df = sample_df()
    assert_frame_equal(df, hex_to_df(df_to_hex(df)))


def test_base64_roundtrip():
    df = sample_df()
    assert_frame_equal(df, base64_to_df(df_to_base64(df)))


def test_dedup_primitives():
    assert dedup([3, 1, 2, 1, 3]) == [3, 1, 2]


def test_dedup_preserves_order():
    assert dedup([3, 1, 2, 1, 3]) == [3, 1, 2]


def test_dedup_with_key():
    items = [{"id": 1, "name": "a"}, {"id": 1, "name": "b"}, {"id": 2, "name": "c"}]
    assert dedup(items, key=lambda x: x["id"]) == [{"id": 1, "name": "a"}, {"id": 2, "name": "c"}]


def test_dedup_unhashable():
    items = [[1, 2], [3, 4], [1, 2]]
    assert dedup(items) == [[1, 2], [3, 4]]


def test_deep_flatten():
    assert deep_flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert deep_flatten([[1, [2, 3]], [4]]) == [1, 2, 3, 4]
    assert deep_flatten([1, [2, [3, [4]]]]) == [1, 2, 3, 4]
    assert deep_flatten(["ab", ["cd"]]) == ["ab", "cd"]
    assert deep_flatten([]) == []


def test_fix_mac_hangul():
    decomposed = "\u1100\u1161"  # 'ㄱ' + 'ㅏ' (NFD)
    result = fix_mac_hangul(decomposed)
    assert result == "가"


def test_create_directory_recursive():
    with tempfile.TemporaryDirectory() as tmp:
        target = Path(tmp) / "a" / "b" / "c"
        create_directory_recursive(str(target))
        assert target.exists()
        assert target.is_dir()
