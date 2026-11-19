linha1 = input()

while linha1 != "0 0":

    n_bilhetes, n_pessoas = map(int, linha1.split())

    frequencia = n_bilhetes * [0]

    linha2 = list(map(int, input().split()))
    for elemento in linha2:
        frequencia[elemento-1] += 1

    contador_clonados = 0

    for elemento in frequencia:
        if elemento > 1:
            contador_clonados += 1
    
    print(contador_clonados)    

    linha1 = input()