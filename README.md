# sugarpowder
Package of Python syntactic sugars inspired by Elixir, Go, Rust, Julia, and other languages


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

Pipes for pandas DataFrame are in development.