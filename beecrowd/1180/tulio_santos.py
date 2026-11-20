n:int = int(input())

vetor:list = list(map(int, input().split()))

menor: int = min(vetor)
posicao: int = int(vetor.index(menor))

print(f"Menor valor: {menor}")
print(f"Posicao: {posicao}")