vetor = []
vetor.append(int(input()))

for i in range(9):
    vetor.append(vetor[i]*2)
    print(f"N[{i}] = {vetor[i]}")
    
print(f"N[9] = {vetor[9]}")


