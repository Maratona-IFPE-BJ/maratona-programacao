valor = float(input())

if valor >= 0 and valor <= 25:
    resposta = "Intervalo [0,25]"
elif valor > 25 and valor <= 50:
    resposta = "Intervalo (25,50]"
elif valor > 50 and valor <= 75:
    resposta = "Intervalo (50,75]"
elif valor > 75 and valor <= 100:
    resposta = "Intervalo (75,100]"
else:
    resposta = "Fora de intervalo"

print(resposta)
