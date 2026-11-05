l1 = input()
l2 = input()
l3 = input()
l4 = input()

diaInicio = int(l1.split(" ")[1])
horaInicio = int(l2.split(":")[0].strip())
minutoInicio = int(l2.split(":")[1].strip())
segundoInicio = int(l2.split(":")[2].strip())
diaFim = int(l3.split(" ")[1])
horaFim = int(l4.split(":")[0].strip())
minutoFim = int(l4.split(":")[1].strip())
segundoFim = int(l4.split(":")[2].strip())

inicio = diaInicio*24*60*60+horaInicio*60*60+minutoInicio*60+segundoInicio
fim = diaFim*24*60*60+horaFim*60*60+minutoFim*60+segundoFim

evento = fim - inicio
dias = int(evento/60/60/24)
evento = evento-(dias*24*60*60)
horas = int(evento/60/60)
evento = evento-(horas*60*60)
minutos = int(evento/60)
segundos = evento-(minutos*60)
print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")
