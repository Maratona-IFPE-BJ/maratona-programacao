n: int = int(input())
for i in range(n):
    dado = input().split()
    dado.sort(key = len, reverse = True)
    print(*dado)