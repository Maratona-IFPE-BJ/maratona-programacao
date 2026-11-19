array = [0] * 10

for i in range(len(array)):
    entrada = int(input())
    if entrada <= 0:
        array[i] = 1
    else:
        array[i] = entrada

for i in range(len(array)):
    print(f"X[{i}] = {array[i]}")
