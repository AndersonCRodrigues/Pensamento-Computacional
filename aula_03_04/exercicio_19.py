"""
Cada degrau de uma escada tem uma altura X. Faça um algoritmo que receba essa
altura e a altura que o usuário deseja alcançar subindo a escada. Calcule e
mostre quantos degraus o usuário deverá subir para atingir seu objetivo.
"""

import math

altura_degrau = float(input("Digite a altura de cada degrau em metros: "))
altura_desejada = float(input("Digite a altura em metros: "))

total_degraus = math.ceil(altura_desejada / altura_degrau)

print(f"Você precisará subir {total_degraus} degraus para atingir a altura.")
