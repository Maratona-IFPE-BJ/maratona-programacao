n = int(input())
alturas = list(map(int, input().split()))

resposta = True

if alturas[0] == alturas[1]:
    resposta = False

for i in range(1, n-1):
    if not((alturas[i - 1] < alturas[i] and alturas[i] > alturas[i + 1]) or
           (alturas[i - 1] > alturas[i] and alturas[i] < alturas[i + 1])):
        resposta = False
        break
    
print(1 if resposta else 0)


