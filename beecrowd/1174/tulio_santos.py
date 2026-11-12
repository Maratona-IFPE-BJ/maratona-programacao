lista: list[float] = []

for i in range(100):
    a = float(input())
    lista.append(a)

for i in range(len(lista)):
    if lista[i] <= 10:
        print(f"A[{i}] = {lista[i]}")
