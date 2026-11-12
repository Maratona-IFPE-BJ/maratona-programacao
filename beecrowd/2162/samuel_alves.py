qt_medicoes:int = int(input())
medicoes:list[int] = list(map(int, input().split()))
controle:str = None
erro:bool = False

for i in range(len(medicoes)):
    if i != 0 :
        if medicoes[i] > medicoes[i -1] and controle != "pico":
            controle = "pico"
        elif medicoes[i] > medicoes[i -1] and controle == "pico":
            erro = True
 
        elif medicoes[i] < medicoes[i -1] and controle != "vale":
            controle = "vale"
        elif medicoes[i] < medicoes[i -1] and controle == "vale":
            erro = True
        elif medicoes[i] == medicoes[i -1] or medicoes[i] == medicoes[i+1]:
            erro = True

if erro:
    print("0")
else:
    print("1")
