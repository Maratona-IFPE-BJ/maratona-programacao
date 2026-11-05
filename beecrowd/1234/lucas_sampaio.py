while True:
    try:
        texto = input()
    except EOFError:
        break

    maiuscula = True
    resultado = ""

    for caractere in texto:
        if caractere == " ":
            resultado += caractere
        else:
            if maiuscula:
                resultado += caractere.upper()
            else:
                resultado += caractere.lower()

            maiuscula = not maiuscula

    print(resultado)
