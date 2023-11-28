def fibonacci_dynamic(n: int) -> int:
    fib_list = [0, 1]

    for _ in range(1, n + 1):
        next = fib_list[0] + fib_list[1]
        fib_list = [fib_list[1], next]
    return fib_list[0]
