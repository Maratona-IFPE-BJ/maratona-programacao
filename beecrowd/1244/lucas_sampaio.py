numero_strings = int(input())

for i in range(numero_strings):
    strings = input().split()
    strings = sorted(strings, key = len, reverse = True)
    print(" ".join(strings))

