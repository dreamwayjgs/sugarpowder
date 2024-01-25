from io import BytesIO
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq


def df_to_parquetstream(df: pd.DataFrame) -> bytes:
    pqstream = BytesIO()
    pq.write_table(pa.Table.from_pandas(df), pqstream)
    pqbytes = pqstream.getvalue()
    return pqbytes


def parquetstream_to_df(pqbytes: bytes) -> pd.DataFrame:
    pqstream = BytesIO(pqbytes)
    pqtable = pq.read_table(pqstream)

    return pqtable.to_pandas()