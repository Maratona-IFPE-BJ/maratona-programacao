lista: list[int] = []

for i in range(10):
    x = int(input())
    if x <= 0:
        lista.append(1)
    else:
        lista.append(x)

for i in range(len(lista)):
    print(f"X[{i}] = {lista[i]}")
