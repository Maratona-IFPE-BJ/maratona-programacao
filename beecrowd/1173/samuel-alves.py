valor:int = int(input())
vetor:list[int] = []
vetor.append(valor)

for i in range(9):
    novo_valor:int = vetor[len(vetor)-1] * 2
    vetor.append(novo_valor)

for i in range(len(vetor)):
    print(f"N[{i}] = {vetor[i]}")

