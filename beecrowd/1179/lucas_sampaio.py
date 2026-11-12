pares = []
impares = []

for i in range(15):

    numero = int(input())
    
    if numero % 2 == 0:
        if len(pares) < 5:
            pares.append(numero)
        else:
            for j in range(len(pares)):
                print(f"par[{j}] = {pares[j]}")
            pares = []
            pares.append(numero)
    else:
        if len(impares) < 5:
            impares.append(numero)
        else:
            for j in range(len(impares)):
                print(f"impar[{j}] = {impares[j]}")
            impares = []
            impares.append(numero)

for i in range(len(impares)):
    print(f"impar[{i}] = {impares[i]}")

for i in range(len(pares)):
    print(f"par[{i}] = {pares[i]}")

