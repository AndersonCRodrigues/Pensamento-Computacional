# Faça um algoritmo que receba o peso e a altura de uma pessoa e calcule o
# índice de massa corpórea. Ele mede a relação entre peso e
# altura (peso em Kg, dividido pelo quadrado da altura em metros).

peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em cm): "))

altura_metros = altura / 100

imc = peso / (altura_metros**2)

print("O Índice de Massa Corporal (IMC) é:", imc)
