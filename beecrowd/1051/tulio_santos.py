dia_inicio = input().strip()
horas_inicio = input().strip()

dia_fim = input().strip()
horas_fim = input().strip()

di = dia_inicio.split()
df = dia_fim.split()

hi = horas_inicio.split(" : ")
hf = horas_fim.split(" : ")

segundos_iniciais = (int(di[1]) * 86400) + (int(hi[0]) * 3600) + (int(hi[1]) * 60) + (int(hi[2]))
segundos_finais = (int(df[1]) * 86400) + (int(hf[0]) * 3600) + (int(hf[1]) * 60) + (int(hf[2]))

diferenca = segundos_finais - segundos_iniciais

dias = diferenca / 86400

diferenca = diferenca % 86400

horas = diferenca / 3600

diferenca = diferenca % 3600

minutos = diferenca / 60

diferenca = diferenca % 60

segundos = diferenca

print(f'{int(dias)} dia(s)\n{int(horas)} hora(s)\n{int(minutos)} minuto(s)\n{int(segundos)} segundo(s)')