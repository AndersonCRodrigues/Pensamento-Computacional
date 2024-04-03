"""
Elabore um algoritmo que leia do teclado uma quantidade de segundos e
transforme este tempo em dias, horas e minutos
"""


def converter_tempo(segundos):
    dias = segundos // (24 * 3600)
    segundos %= 24 * 3600
    horas = segundos // 3600
    segundos %= 3600
    minutos = segundos // 60
    segundos %= 60

    return dias, horas, minutos, segundos


segundos = int(input("Digite a quantidade de segundos: "))


dias, horas, minutos, segundos_restantes = converter_tempo(segundos)


print(
    f"{segundos} segundos correspondem a {dias} dias, "
    f"{horas} horas, {minutos} minutos e {segundos_restantes} segundos."
)
