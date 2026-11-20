fib = [0, 1]
for i in range(2, 61):
    fib.append(fib[i - 1] + fib[i - 2])

quantidade = int(input())

for _ in range(quantidade):
    p = int(input())
    print(f"Fib({p}) = {fib[p]}")