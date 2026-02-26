from typing import NamedTuple

import pandas as pd


class DateStats(NamedTuple):
    min: pd.Timestamp
    max: pd.Timestamp
    nunique: int


def date_stats(df: pd.DataFrame, date_col: str = 'date') -> DateStats:
    return DateStats(
        min=df[date_col].min(),
        max=df[date_col].max(),
        nunique=df[date_col].nunique(),
    )
