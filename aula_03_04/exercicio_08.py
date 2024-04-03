"""
Faça o algoritmo que calcule o valor em Reais, correspondente aos dólares que
um turista possui no cofre do hotel. O programa deve solicitar os seguintes
dados: Quantidade de dólares guardados no cofre e cotação do dólar naquele dia.
"""


def conversao(dolar, cotacao):
    return dolar * cotacao


valor = float(input("Entre com o valor em dolar: $ "))
taxa = float(input("Entre com a taxa de cambio: "))

real = conversao(valor, taxa)

print(f"$ {valor} a uma taxa de {taxa} valem R$ {real}")
