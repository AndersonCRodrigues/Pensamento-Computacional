"""
 A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco) prestações
 sem juros. Faça um algoritmo que receba um valor de uma compra e mostre o
 valor das prestações
"""

valor = float(input("Entre com o valor a ser calculado: R$ "))

prestação = valor / 5

print(
    f"O valor de R$ {valor:.2f} pode ser dividido"
    f"em 5 parcelas de R$ {prestação:.2f}"
    )
