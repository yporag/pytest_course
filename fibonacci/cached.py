from fibonacci.naive import fibonacci_naive
from functools import lru_cache

cache = {}


def fibonacci_cached(n: int) -> int:
    if n in cache:
        return cache[n]
    res = fibonacci_naive(n)

    cache[n] = res
    return res


@lru_cache(maxsize=256)
def fib_lru_cached(n: int) -> int:
    return fibonacci_naive(n)
