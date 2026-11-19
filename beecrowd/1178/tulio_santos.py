vetor = [0] * 100

x: float = float(input())
vetor[0] = x

for i in range(1,100):
    vetor[i] = vetor[i-1] / 2

for j in range(100):
    print(f"N[{j}] = {vetor[j]:.4f}")