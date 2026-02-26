from datetime import datetime, timedelta

import pandas as pd


def daterange(base: datetime = datetime.now(), days=7):
    return [base + timedelta(days=x) for x in range(days)]

def summary_date(df: pd.DataFrame, date_col: str='date'):
    return df[date_col].min(), df[date_col].max(), df[date_col].nunique()
