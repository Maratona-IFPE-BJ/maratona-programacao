n_testes:int = int(input())

for i in range(n_testes):
    palavras:list[str] = input().split()
    palavras.sort(key=len, reverse=True)
    print(" ".join(palavras))