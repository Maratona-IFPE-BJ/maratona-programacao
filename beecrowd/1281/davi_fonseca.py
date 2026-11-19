lista_de_produtos = []
lista_de_somas = []

quantidade_de_saidas = int(input())

for i in range(quantidade_de_saidas):
    quant_produtos_mercado = int(input())

    for j in range(quant_produtos_mercado):
        
        produtos_mercado = input().split()
        preco = float(produtos_mercado[1])
        
        produto = {
            "nome": produtos_mercado[0],
            "preco": preco
        }
        lista_de_produtos.append(produto)

    quant_produtos_escolhidos = int(input())
    somador = 0

    for k in range(quant_produtos_escolhidos):

        produtos_escolhidos = input().split()
        quantidade = list(map(int, produtos_escolhidos[1]))
        for i in range(len(lista_de_produtos)):
            if produtos_escolhidos[0] == lista_de_produtos[i]["nome"]:
                soma = quantidade[0] * lista_de_produtos[i]["preco"]
                somador += soma

    lista_de_somas.append(somador)
    lista_de_produtos = []        

for i in range(len(lista_de_somas)):
    print(f"R$ {lista_de_somas[i]:.2f}")


    