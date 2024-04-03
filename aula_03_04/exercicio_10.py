"""
Ler uma temperatura em graus Celsius e apresenta-la convertida em graus
Fahrenheit. A fórmula de conversão é: F=(9*C+160) / 5, sendo F a
temperatura em Fahrenheit e C a temperatura em Celsius.
"""


def converte_fahrenheit(c):
    return (9 * c + 160) / 5


celcius = float(input("Entre com uma temperatura em graus celcius: "))

fahrenheit = converte_fahrenheit(celcius)

print(f"{celcius}º C equivale a {fahrenheit}º F")
