while True:
    try:
        linha = input()

        maiuscula = True

        linha_final = ""

        for c in linha:
            if c == ' ':
                linha_final += c
            else:
                if maiuscula:
                    c = c.upper()
                    linha_final += c
                    maiuscula = False
                elif not maiuscula:
                    c = c.lower()
                    linha_final += c
                    maiuscula = True

        print(linha_final)

    except EOFError:
        break  # Esta é a sua condição de parada (Erro de fim de arquivo)