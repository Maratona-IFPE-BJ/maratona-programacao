n: int = int(input())
entrada = input().split()

lista = [int(val) for val in entrada]

resultado = 1

if n == 2:
    if lista[0] == lista[1]:
        resultado = 0
else:
    for i in range(1, n - 1):
        anterior = lista[i - 1]
        atual = lista[i]
        proximo = lista[i + 1]

        if atual > anterior and atual > proximo:
            pass
        elif atual < anterior and atual < proximo:
            pass
        else:
            resultado = 0
            break

print(resultado)