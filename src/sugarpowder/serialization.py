import base64
import pickle
from io import BytesIO
from os import PathLike
from typing import Any

import blosc
import dill
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq


def df_to_parquetstream(df: pd.DataFrame) -> bytes:
    pqstream = BytesIO()
    pq.write_table(pa.Table.from_pandas(df), pqstream)
    return pqstream.getvalue()


def parquetstream_to_df(pqbytes: bytes) -> pd.DataFrame:
    pqstream = BytesIO(pqbytes)
    return pq.read_table(pqstream).to_pandas()


def df_to_hex(df: pd.DataFrame) -> str:
    return df_to_parquetstream(df).hex()


def hex_to_df(hexed_df: str) -> pd.DataFrame:
    return parquetstream_to_df(bytes.fromhex(hexed_df))


def df_to_base64(df: pd.DataFrame) -> bytes:
    return base64.b64encode(df_to_parquetstream(df))


def base64_to_df(base64_df: bytes) -> pd.DataFrame:
    return parquetstream_to_df(base64.b64decode(base64_df))


def blosc_pickle(obj: Any, file: str | PathLike[str] | None = None) -> bytes:
    compressed = blosc.compress(pickle.dumps(obj))
    if file is not None:
        with open(file, "wb") as f:
            f.write(compressed)
    return compressed


def blosc_unpickle(
    data: str | bytes | None = None, file: str | PathLike[str] | None = None
):
    if data is not None:
        return pickle.loads(blosc.decompress(data))
    if file is not None:
        with open(file, "rb") as f:
            return pickle.loads(blosc.decompress(f.read()))
    raise Exception("Either 'data' or 'file' must be provided, but both were None.")


def blosc_dill(obj: Any, file: str | PathLike[str] | None = None) -> bytes:
    compressed = blosc.compress(dill.dumps(obj))
    if file is not None:
        with open(file, "wb") as f:
            f.write(compressed)
    return compressed


def blosc_undill(
    data: str | bytes | None = None, file: str | PathLike[str] | None = None
):
    if data is not None:
        return dill.loads(blosc.decompress(data))
    if file is not None:
        with open(file, "rb") as f:
            return dill.loads(blosc.decompress(f.read()))
    raise Exception("Either 'data' or 'file' must be provided, but both were None.")
