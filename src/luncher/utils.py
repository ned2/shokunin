from typing import TextIO, Callable
from time import time
from contextlib import contextmanager


@contextmanager
def timing(
    description: str = "Code execution", echo_func: Callable = print, echo: bool = True
) -> None:
    start = time()
    yield
    ellapsed_time = time() - start
    if echo:
        echo_func(f"{description}: {ellapsed_time:.2f} seconds")
