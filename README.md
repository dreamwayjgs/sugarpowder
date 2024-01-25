# sugarpowder
Package of Python syntactic sugars and utils inspired by Elixir, Go, Rust, Julia, and other languages


## Utils

df_to_parquetstream, parquetstream_to_df: Convert pandas Dataframe <--> parquetfile bytes stream

## WithErr
Go lang Style error handling

```
@witherr
def div1(x: float, y: float) -> float:
    """
    test function - divide
    """
    return x / y


val, err = div1(1, 1)
# val == 1, err is None

val, err = div1(1, 0)
# val is None, err == ZeroDivisionError

```


## Pipe
Forked from [Pipe Package](https://github.com/JulienPalard/Pipe)

It works on '|' and '>>' both.