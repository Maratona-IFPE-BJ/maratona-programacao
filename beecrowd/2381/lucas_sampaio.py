num_alunos, num_sorteado = map(int, input().split())

alunos = []

for i in range(num_alunos):
    alunos.append(input())
 
alunos.sort()

print(alunos[num_sorteado - 1])