"""
Faça um algoritmo que receba o ano de nascimento de uma pessoa e o ano atual,
calcule e mostre:
a. A idade dessa pessoa;
b. Quantos anos ela terá em 2028.
"""


def calcular_idade(ano_nascimento, ano_atual):
    idade_atual = ano_atual - ano_nascimento
    idade_2028 = 2028 - ano_nascimento
    return idade_atual, idade_2028


ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade_atual, idade_2028 = calcular_idade(ano_nascimento, ano_atual)

print(f"A idade atual é: {idade_atual} anos")
print(f"Em 2028, essa pessoa terá: {idade_2028} anos")
