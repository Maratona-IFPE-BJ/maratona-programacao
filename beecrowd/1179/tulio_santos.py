par: list[int] = []
impar: list[int] = []
i: int = 0

while i < 15:
    entrada = int(input())

    if entrada % 2 == 0:
        if len(par) == 5:
            for r in range(5):
                print(f"par[{r}] = {par[r]}")
            par.clear()
        par.append(entrada)
    else:
        if len(impar) == 5:
            for j in range(5):
                print(f"impar[{j}] = {impar[j]}")
            impar.clear()
        impar.append(entrada)

    i += 1

for k in range(len(impar)):
    print(f"impar[{k}] = {impar[k]}")

for l in range(len(par)):
    print(f"par[{l}] = {par[l]}")