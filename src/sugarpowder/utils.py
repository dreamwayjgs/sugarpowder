from io import BytesIO
from typing import Iterable, TypeVar
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq


T = TypeVar('T')


def df_to_parquetstream(df: pd.DataFrame) -> bytes:
    pqstream = BytesIO()
    pq.write_table(pa.Table.from_pandas(df), pqstream)
    pqbytes = pqstream.getvalue()
    return pqbytes


def parquetstream_to_df(pqbytes: bytes) -> pd.DataFrame:
    pqstream = BytesIO(pqbytes)
    pqtable = pq.read_table(pqstream)

    return pqtable.to_pandas()


def deduplist(seq: Iterable[T], keep_order=True) -> list[T]:
    if keep_order:
        return list(dict.fromkeys(seq))
    return list(set(seq))
