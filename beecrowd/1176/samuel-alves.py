entrada:int = int(input())
fibonnaci:list[int]  = [0,1]

for i in range(59):
    novo_numero:int = fibonnaci[-1] + fibonnaci[-2]
    fibonnaci.append(novo_numero)

for i in range(entrada):
    fib_index:int = int(input())
    print(f"Fib({fib_index}) = {fibonnaci[fib_index]}")

