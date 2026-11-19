n, m = map(int, input().split())
vetor:list = []

for i in range(n):
    vetor.append((input().strip()))

vetor.sort()

print(vetor[m - 1])