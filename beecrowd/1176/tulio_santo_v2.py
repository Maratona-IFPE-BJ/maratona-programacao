from functools import cache

@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

quantidade = int(input())
for _ in range(quantidade):
    p = int(input())
    print(f"Fib({p}) = {fibonacci(p)}")
