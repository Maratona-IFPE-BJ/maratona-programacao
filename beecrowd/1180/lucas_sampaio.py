num_elementos = int(input())
elementos = list(map(int, input().split()))

menor_valor = elementos[0]
posicao = 0

for i in range(1, num_elementos):
    if elementos[i] < menor_valor:
        menor_valor = elementos[i]
        posicao = i

print(f"""Menor valor: {menor_valor}
Posicao: {posicao}""")
