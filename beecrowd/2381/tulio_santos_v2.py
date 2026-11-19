n, m = map(int, input().split())
vetor: list = []

for i in range(n):
    vetor.append(input().strip())

# Ordenação manual (Selection Sort) no lugar de vetor.sort()
for i in range(n):
    indice_menor = i
    for j in range(i + 1, n):
        if vetor[j] < vetor[indice_menor]:
            indice_menor = j
    vetor[i], vetor[indice_menor] = vetor[indice_menor], vetor[i]

print(vetor[m - 1])