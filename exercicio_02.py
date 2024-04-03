"""
Faça um algoritmo que o usuário informe os valores dos catetos
de um triângulo retângulo e que ao final escreva a sua
hipotenusa.
"""

import math


cat01 = float(input("Entre com o primeiro cateto: "))
cat02 = float(input("Entre com o segundo cateto: "))

hipotenusa = math.sqrt((cat01**2) + (cat02**2))

print(f"A hipotenusa dos catetos informados é de {hipotenusa}")
