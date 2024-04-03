"""
Faça um algoritmo que receba o valor de um depósito e o valor da taxa de juros,
calcule e mostre o valor do rendimento e o valor total depois do rendimento.
"""


def calcular_rendimento(depósito, taxa_juros):
    rendimento = depósito * taxa_juros / 100
    total_após_rendimento = depósito + rendimento
    return rendimento, total_após_rendimento


deposito = float(input("Digite o valor do depósito: "))
taxa_juros = float(input("Digite a taxa de juros (%): "))

rendimento, total_após_rendimento = calcular_rendimento(deposito, taxa_juros)

print(
    f"O rendimento será de R$ {rendimento:.2f}"
    f"O valor total pós rendimento será de R$ {total_após_rendimento:.2f}"
)
