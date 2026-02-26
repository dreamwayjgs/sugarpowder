from datetime import datetime

import pandas as pd

from sugarpowder.dates import date_stats


def test_date_stats():
    df = pd.DataFrame({
        "date": [datetime(2024, 1, 1), datetime(2024, 1, 3), datetime(2024, 1, 3), datetime(2024, 1, 5)],
    })
    result = date_stats(df)
    assert result.min == datetime(2024, 1, 1)
    assert result.max == datetime(2024, 1, 5)
    assert result.nunique == 3


def test_date_stats_custom_col():
    df = pd.DataFrame({
        "created_at": [datetime(2024, 3, 1), datetime(2024, 3, 5)],
    })
    result = date_stats(df, date_col="created_at")
    assert result.min == datetime(2024, 3, 1)
    assert result.max == datetime(2024, 3, 5)
    assert result.nunique == 2
