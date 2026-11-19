qtd_idas = int(input())
for i in range(qtd_idas):
    qtd_produtos = int(input())
    produtos_valores = []
    for j in range(qtd_produtos):
        produtos_valores.append(input().split())

    valor_total = 0.0

    qtd_comprados = int(input())
    for i in range(qtd_comprados):
        produto, quantidade = input().split()
        for elemento in produtos_valores:
            if elemento[0] == produto:
                valor_total += int(quantidade) * (float(elemento[1]))
    print(f"R$ {valor_total:.2f}")


    
        



