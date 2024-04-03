"""
O custo ao consumidor de um carro novo é a soma do custo de fábrica com a
percentagem do distribuidor e dos impostos (aplicados, primeiro os impostos
sobre o custo de fábrica, e depois a percentagem do distribuidor sobre o
resultado). Supondo que a percentagem do distribuidor seja de 28% e os
impostos 45%. Escrever um algoritmo que leia o custo de fábrica de um carro e
informe o custo ao consumidor do mesmo.
"""


def calculo_final(valor):
    return (valor * 1.45) * 1.28


valor = float(input("Entre com o valor de fábrica: R$ "))

calc = calculo_final(valor)

print(f"O veículo tem o valor final de R$ {calc:.2f}")
