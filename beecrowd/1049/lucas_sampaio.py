p1 = input()
p2 = input()
p3 = input()

if p1 == "vertebrado":
    if p2 == "ave":
        if p3 == "carnivoro":
            resposta = "aguia"
        else: 
            resposta = "pomba"    
    else:
        if p3 == "onivoro":
            resposta = "homem"
        else: 
            resposta = "vaca"    
else:
    if p2 == "inseto":
        if p3 == "hematofago":
            resposta = "pulga"
        else: 
            resposta = "lagarta"    
    else:
        if p3 == "hematofago":
                resposta = "sanguessuga"
        else: 
            resposta = "minhoca"
print(resposta)