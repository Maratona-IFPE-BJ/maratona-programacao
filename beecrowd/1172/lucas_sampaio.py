vetor = []

for i in range(10):
    vetor.append(int(input()))

for i in range(len(vetor)):
    if vetor[i] <= 0:
        print(f"X[{i}] = 1")
    else: 
        print(f"X[{i}] = {vetor[i]}")