import pytest
from typing import Callable
from fibonacci.cached import fibonacci_cached, fib_lru_cached
from fibonacci.dynamic import fibonacci_dynamic
from fibonacci.naive import fibonacci_naive


@pytest.mark.parametrize("n,expected", [(0, 0), (1, 1), (2, 1), (20, 6765)])
@pytest.mark.parametrize(
    "fib_func", [fibonacci_naive, fibonacci_cached, fib_lru_cached, fibonacci_dynamic]
)
def test_fibonacci(
    time_tracker, fib_func: Callable[[int], int], n: int, expected: int
) -> None:
    res = fib_func(n)
    assert res == expected
