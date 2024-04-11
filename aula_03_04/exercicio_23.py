# Sabe-se que o quilowatt de energia custa um quinto do salário mínimo.
# Faça um algoritmo que receba o valor do salário mínimo e a quantidade de
# quilowatts consumida por uma residência. Calcule e mostre:

# a. O valor, em Reais, de cada quilowatt.
# b. O valor, em Reais, a ser pago por essa residência.
# c. O valor, em Reais, a ser pago com desconto de 15%.

salario_minimo = float(input("Digite o valor do salário mínimo: R$ "))
quilowatts_consumidos = float(
    input("Digite a quantidade de quilowatts consumidos pela residência: ")
)

valor_quilowatt = salario_minimo / 5

valor_total = valor_quilowatt * quilowatts_consumidos

desconto = 0.15
valor_desconto = valor_total * (1 - desconto)

print("\nResultados:")
print(f"a. O valor de cada quilowatt é: R${valor_quilowatt:.2f}")
print(f"b. O valor a ser pago pela residência é: R${valor_total:.2f}")
print(f"c. O valor a ser pago com desconto de 15% é: R${valor_desconto:.2f}")
