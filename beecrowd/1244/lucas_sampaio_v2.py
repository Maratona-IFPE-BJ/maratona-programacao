casos_teste = int(input())

for i in range(casos_teste):
    palavras = input().split()

    for j in range(len(palavras)):
        for k in range(len(palavras) - 1 - j):

            if len(palavras[k]) < len(palavras[k + 1]):
                palavras[k], palavras[k + 1] = palavras[k + 1], palavras[k]

    print(" ".join(palavras))
