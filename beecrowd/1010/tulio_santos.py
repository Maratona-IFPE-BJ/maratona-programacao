# Lê a primeira linha, divide os valores pelos espaços e atribui às variáveis
linha1 = input().split()
cod_1 = int(linha1[0])
quant_1 = int(linha1[1])
valor_unit_1 = float(linha1[2])

# Lê a segunda linha, divide os valores pelos espaços e atribui às variáveis
linha2 = input().split()
cod_2 = int(linha2[0])
quant_2 = int(linha2[1])
valor_unit_2 = float(linha2[2])

# Calcula o valor total a pagar
resultado = (valor_unit_1 * quant_1) + (valor_unit_2 * quant_2)

# Exibe o resultado formatado com duas casas decimais
print(f"VALOR A PAGAR: R$ {resultado:.2f}")

# utilizando map:

# Lê a linha, separa por espaços e converte tudo para float ao mesmo tempo
cod_1, quant_1, valor_unit_1 = map(float, input().split())

# Faz o mesmo para a segunda linha
cod_2, quant_2, valor_unit_2 = map(float, input().split())

# O cálculo continua igual
resultado = (quant_1 * valor_unit_1) + (quant_2 * valor_unit_2)

# Exibe o resultado
print(f"VALOR A PAGAR: R$ {resultado:.2f}")