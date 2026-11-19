fibonacci = [0, 1]

casos_teste = int(input())

for i in range(casos_teste):
    numero = int(input())

    while numero > len(fibonacci) - 1:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
        
    print(f"Fib({numero}) = {fibonacci[numero]}") 
        
        
        