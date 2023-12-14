import time
from functools import lru_cache
from typing import Generator


def timerfunc(func):
    """
    A timer decorator
    """
    def function_timer(*args, **kwargs):
        """
        A nested function for timing other functions
        """
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        msg = "{func}()) : {time} s"
        print(msg.format(func=func.__name__,
                         time=runtime))
        return value
    return function_timer


@lru_cache(maxsize=None)
def fib1(n: int) -> int:
    # print(n, end=' ')
    if n < 3:
        return 1
    return fib1(n - 2) + fib1(n - 1)


@timerfunc
def fib1_wrapper(n: int) -> int:
    return fib1(n)


@timerfunc
def fib2(n: int) -> int:
    prev: int = 0
    curr: int = 1
    for _ in range(1, n):
        prev, curr = curr, prev + curr
    return curr


def fib_gen(n: int) -> Generator[int, None, None]:
    prev: int = 0
    curr: int = 1
    for _ in range(1, n):
        prev, curr = curr, prev + curr
        yield curr


# print(fib1_wrapper(1000))
# print(fib2(1000))

# for i in fib_gen(100):
#     print(i, end=' ')
