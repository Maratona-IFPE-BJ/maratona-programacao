n, m = map(int, input().split())
vetor = [input().strip() for _ in range(n)]

for _ in range(m - 1):
    vetor.remove(min(vetor))

print(min(vetor))