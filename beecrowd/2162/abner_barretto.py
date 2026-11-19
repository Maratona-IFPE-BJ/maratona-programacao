numeroMedida = int(input())
alturaCadaMedida = list(map(int, input().split()))

confirmacao = True

if numeroMedida == 2 and alturaCadaMedida[0] == alturaCadaMedida[1]:
    confirmacao = False
    
if numeroMedida < 2:
  confirmacao = False
else:
  for i in range(1, numeroMedida - 1):
    if alturaCadaMedida[i] > alturaCadaMedida[i-1] and alturaCadaMedida[i] > alturaCadaMedida[i+1]:
      confirmacao = True
    elif alturaCadaMedida[i] < alturaCadaMedida[i-1] and alturaCadaMedida[i] < alturaCadaMedida[i+1]:
      confirmacao = True
    else:
      confirmacao = False
      break

if confirmacao:
  print(1)
else:
  print(0)
