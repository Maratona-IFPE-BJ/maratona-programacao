vetor: list[int] = [0] * 10
v: int = int(input())
vetor[0] = v

for i in range(1,10):
    vetor[i] = vetor[i-1] * 2

for i in range(10):
    print(f"N[{i}] = {vetor[i]}")