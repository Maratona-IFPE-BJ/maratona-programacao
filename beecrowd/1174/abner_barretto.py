array = [0] * 100

for i in range(len(array)):
    entrada  = float(input())
    array[i] = entrada


for i in range(len(array)):
    if array[i] <= 10:
        print(f"A[{i}] = {array[i]:.1f}")
