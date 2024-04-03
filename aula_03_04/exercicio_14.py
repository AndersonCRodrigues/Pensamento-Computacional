"""
Elabore um algoritmo que leia o tamanho do lado de um quadrado e informe a
área e o perímetro do quadrado. (Perímetro = 4 * L; área = L ^ 2).
"""

lado = int(input("Entre com um numero inteiro para o lado do quadrado: "))

perimeto = 4 * lado
area = lado**2

print(f"O Quadrado informado tem perimero de {perimeto} e área de {area}")
