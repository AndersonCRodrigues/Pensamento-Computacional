"""
Faça um algoritmo que calcule as raízes de ax²+bx+c (sqr), pressupondo que
seu delta sempre será positivo e sempre terá uma raiz exata
"""

import math


def calcular_raizes(a, b, c):
    discriminante = b**2 - 4 * a * c
    raiz_delta = math.sqrt(discriminante)

    x1 = (-b + raiz_delta) / (2 * a)
    x2 = (-b - raiz_delta) / (2 * a)

    return x1, x2


numA = int(input("Entre com o valor de A: "))
numB = int(input("Entre com o valor de B: "))
numC = int(input("Entre com o valor de C: "))

x1, x2 = calcular_raizes(numA, numB, numC)
print(f"Raízes da equação ({numA}x²) + ({numB}x) + ({numC}):", x1, "e", x2)
