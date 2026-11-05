# -*- coding: utf-8 -*-

# Lê as 3 palavras, uma em cada linha
p1 = input().strip()
p2 = input().strip()
p3 = input().strip()

if p1 == "vertebrado":
    if p2 == "ave":
        if p3 == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    elif p2 == "mamifero":
        if p3 == "onivoro":
            print("homem")
        else:
            print("vaca")

elif p1 == "invertebrado":
    if p2 == "inseto":
        if p3 == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    elif p2 == "anelideo":
        if p3 == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")