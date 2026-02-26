# sugarpowder

A humble collection of Python utilities for data processing, serialization, and everyday patterns.

## Install

```
pip install sugarpowder
```

## Test

```
uv run pytest tests/
```

---

## Serialization

Compressed pickle/dill and DataFrame serialization utilities.

```python
from sugarpowder.serialization import (
    blosc_pickle, blosc_unpickle,   # pickle + blosc compression
    blosc_dill, blosc_undill,       # dill + blosc compression (supports lambdas)
    df_to_parquetstream, parquetstream_to_df,
    df_to_hex, hex_to_df,
    df_to_base64, base64_to_df,
)

# Any Python object
data = blosc_pickle(obj)
obj = blosc_unpickle(data)

# Lambda / closure (dill)
data = blosc_dill(lambda x: x * 2)
fn = blosc_undill(data)

# DataFrame <-> bytes
pqbytes = df_to_parquetstream(df)
df = parquetstream_to_df(pqbytes)
```

---

## Lists

```python
from sugarpowder.lists import dedup, deep_flatten

# Dedup while preserving order
dedup([3, 1, 2, 1, 3])                                        # [3, 1, 2]
dedup([{"id": 1}, {"id": 1}, {"id": 2}], key=lambda x: x["id"])  # [{"id": 1}, {"id": 2}]

# Deep flatten
deep_flatten([1, [2, [3, [4]]]])  # [1, 2, 3, 4]
```

---

## Strings

```python
from sugarpowder.strings import fix_mac_hangul, strip_invisible

# Fix NFD Korean from macOS
fix_mac_hangul("ㄱㅏ")  # "가"

# Remove hidden Unicode characters (zero-width space, BOM, etc.)
strip_invisible("hello\u200bworld")  # "helloworld"
```

---

## Dates

```python
from sugarpowder.dates import date_stats

result = date_stats(df, date_col="date")
result.min      # earliest date
result.max      # latest date
result.nunique  # number of unique dates
```

---

## pmap

Parallel element-wise map using multiprocessing.

```python
from sugarpowder.pmap import pmap

pmap(add, [1, 2, 3], [4, 5, 6])               # [5, 7, 9]
pmap(add, [1, 2, 3], [4, 5, 6], num_workers=4)
```

---

## tick

Lap timer for measuring elapsed time between checkpoints.

```python
from sugarpowder.tick import tick

t = tick()
# ... work ...
t = tick(t, label="step 1")             # [main:10] Elapsed step 1: 0.1234s
t = tick(t, label="step 2", msg="done") # [main:12] Elapsed step 2: 0.0234s / done
```

---

## Pipes (removed in v2.0)

Use the [`pipe`](https://pypi.org/project/pipe/) package instead.
