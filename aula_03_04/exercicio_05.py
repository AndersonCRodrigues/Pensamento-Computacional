"""
Uma pessoa resolveu fazer uma aplicação em uma poupança programada.
Para calcular seu rendimento, ela deverá fornecer o valor constante da
aplicação mensal, a taxa e o número de meses. Sabendo-se que a fórmula
usada para este cálculo é:
"""


def calculo_poupanca(p, i, n):
    calc = (p * (1 + i) ** (n - 1)) / 7
    return calc


valor = float(input("Entre com o valor a ser aplicar mensalmente: R$ "))
taxa = float(input("Entre com a taxa a ser aplicada: "))
meses = int(input("Entre com o número de meses: "))

aplicacao = calculo_poupanca(valor, taxa, meses)

print(
    f"O valor de R$ {valor}, "
    f"aplicado a uma taxa de {taxa}% ao longo de {meses} meses, "
    f"renderá R$ {aplicacao:.2f}"
)
