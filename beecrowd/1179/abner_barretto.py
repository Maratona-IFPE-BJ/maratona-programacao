par = []
impar = []

for i in range(15):
    entrada = int(input())
    if entrada % 2 == 0:
        par.append(entrada)
    else:
        impar.append(entrada)

    if len(par) == 5:
        for j in range(len(par)):
            print(f"par[{j}] = {par[j]}")
        par.clear()

        
    if len(impar) == 5:
        for j in range(len(impar)):
            print(f"impar[{j}] = {impar[j]}")
        impar.clear()

for j in range(len(impar)):
    print(f"impar[{j}] = {impar[j]}")

for j in range(len(par)):
    print(f"par[{j}] = {par[j]}")
