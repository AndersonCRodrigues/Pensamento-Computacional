"""
Faça um algoritmo que receba o preço de custo de um produto e mostre o valor
de venda. Sabe-se que o preço de custo receberá um acréscimo de acordo com um
percentual informado pelo usuário.
"""

valor = float(input("Enter com o valor do produto; R$ "))
taxa = float(input("Entre com o percentual de acrescimo: "))

ajuste = valor + (valor * taxa / 100)

print(f"O valor com acrescimo é de R$ {ajuste:.2f}")
