import tempfile
from datetime import datetime
from pathlib import Path

import pandas as pd
from pandas.testing import assert_frame_equal

from sugarpowder.utils import (
    df_to_parquetstream,
    parquetstream_to_df,
    df_to_hex,
    hex_to_df,
    df_to_base64,
    base64_to_df,
    deduplist,
    deep_flatten,
    fix_mac_hangul,
    create_directory_recursive,
)


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


def test_deduplist_keep_order():
    result = deduplist([3, 1, 2, 1, 3])
    assert result == [3, 1, 2]


def test_deduplist_no_order():
    result = deduplist([3, 1, 2, 1, 3], keep_order=False)
    assert set(result) == {1, 2, 3}
    assert len(result) == 3


def test_deep_flatten():
    assert deep_flatten([[1, 2], [3, 4]]) == [1, 2]
    assert deep_flatten([1, 2, 3]) == 1
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
