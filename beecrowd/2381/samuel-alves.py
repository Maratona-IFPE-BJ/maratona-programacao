sorteio:list[int] = tuple(map(int,input().split()))
alunos:list[str] = []

for i in range(sorteio[0]):
    nome:str = input()
    alunos.append(nome)

alunos.sort()

print(alunos[sorteio[1] -1])