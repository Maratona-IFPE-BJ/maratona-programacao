n: int = int(input())

pares: list[int] = []
impares: list[int] = []

for i in range(n):
    num: int = int(input())

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

pares.sort()
impares.sort(reverse=True)

for j in range(len(pares)):
    print(pares[j])
for k in range(len(impares)):
    print(impares[k])

