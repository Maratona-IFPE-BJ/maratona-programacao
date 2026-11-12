n = int(input())

for _ in range(n):
    m = int(input())
    precos = {}

    for _ in range(m):
        produto, valor = input().split()
        precos[produto] = float(valor)

    p = int(input())
    total = 0.0

    for _ in range(p):
        produto, qtd = input().split()
        total += precos[produto] * int(qtd)

    print(f"R$ {total:.2f}")