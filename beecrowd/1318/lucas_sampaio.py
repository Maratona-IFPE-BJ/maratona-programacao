linha1 = input()

while linha1 != "0 0":

    bilhetes_unicos = []
    bilhetes_clonados =[]

    linha2 = input().split()

    for elemento in linha2:
        if elemento not in bilhetes_unicos:
            bilhetes_unicos.append(elemento)
        elif elemento not in bilhetes_clonados:
            bilhetes_clonados.append(elemento)

    print(len(bilhetes_clonados))

    linha1 = input()
