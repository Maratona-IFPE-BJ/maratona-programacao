qtd = int(input())
listaNumero = []

for i in range(qtd):
    numero = int(input())
    listaNumero.append(numero)

pares = [x for x in listaNumero if x % 2 == 0]
impares = [x for x in listaNumero if x % 2 != 0]

pares.sort()
impares.sort(reverse=True)

for numero in pares:
    print(numero)

for numero in impares:
    print(numero)
