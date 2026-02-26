from datetime import datetime

import pandas as pd

from sugarpowder.dates import daterange, summary_date


def test_daterange_default_length():
    result = daterange(datetime(2024, 1, 1))
    assert len(result) == 7


def test_daterange_custom_days():
    result = daterange(datetime(2024, 1, 1), days=3)
    assert len(result) == 3
    assert result[0] == datetime(2024, 1, 1)
    assert result[1] == datetime(2024, 1, 2)
    assert result[2] == datetime(2024, 1, 3)


def test_summary_date():
    df = pd.DataFrame({
        "date": [datetime(2024, 1, 1), datetime(2024, 1, 3), datetime(2024, 1, 3), datetime(2024, 1, 5)],
    })
    min_date, max_date, nunique = summary_date(df)
    assert min_date == datetime(2024, 1, 1)
    assert max_date == datetime(2024, 1, 5)
    assert nunique == 3
