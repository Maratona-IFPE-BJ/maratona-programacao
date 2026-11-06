salario: float = float(input())

s_isento: float = 2000.00
primeira_faixa: float = 1000

if salario <= s_isento:
    print("Isento")
elif salario > s_isento:
    if salario <= 3000.00:
        diferenca: float = salario - s_isento
        imposto: float = diferenca * 0.08
        print(f"R$ {imposto:.2f}")
    elif salario <= 4500.00:
        diferenca: float = salario - s_isento
        segunda_faixa: float = diferenca - primeira_faixa
        imposto: float = (primeira_faixa * 0.08) + (segunda_faixa * 0.18)
        print(f"R$ {imposto:.2f}")
    else:
        imposto: float = (primeira_faixa * 0.08) + (1500.00 * 0.18) + ((salario - 4500) * 0.28)
        print(f"R$ {imposto:.2f}")