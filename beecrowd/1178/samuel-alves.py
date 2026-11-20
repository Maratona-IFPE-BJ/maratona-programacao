numero:float = float(input())
numeros:list[float] = []
numeros.append(numero)

for i in range(99):
    numero_metade:float = numeros[-1] / 2 
    numeros.append(numero_metade)

for i in range(len(numeros)):
    print(f"N[{i}] = {numeros[i]:.4f}")