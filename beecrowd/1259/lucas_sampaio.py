n = int(input())

lista_pares = []
lista_impares = []

for i in range(n):
    valor = int(input())
    if valor % 2 == 0:
        lista_pares.append(valor) 
    else:
        lista_impares.append(valor)
        
lista_pares.sort()
lista_impares.sort(reverse=True)

for valor in lista_pares:
    print(valor)
    
for valor in lista_impares:
    print(valor)
    
