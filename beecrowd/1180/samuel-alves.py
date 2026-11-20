len_lista:int = int(input())

numeros:list[int] = list(map(int, input().split()))
menor:int = numeros[0]


for i in range(len_lista):
    if numeros[i] < menor:
        menor = numeros[i]


posicao:int = numeros.index(menor)

print(f"Menor valor: {menor}")
print(f"Posicao: {posicao}")