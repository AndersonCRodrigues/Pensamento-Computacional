"""
Faça um algoritmo que leia quatro números informados pelo
usuário e que depois imprima a média ponderada, sabendo-se
que os pesos são respectivamente: 1, 2, 3 e 4:
"""

num01 = int(input("Informe um número: "))
num02 = int(input("Informe um número: "))
num03 = int(input("Informe um número: "))
num04 = int(input("Informe um número: "))

med = (num01 + num02 + num03 + num04) / 4

print(f"A média dos números informados é {med}")
