vetor = []
vetor.append(float(input()))

for i in range(99):
    vetor.append(vetor[i]/2)
    print(f"N[{i}] = {vetor[i]:.4f}")
    
print(f"N[99] = {vetor[99]:.4f}")