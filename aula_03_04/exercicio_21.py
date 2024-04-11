# Construa um algoritmo que solicite a entrada de dois números
# inteiros e calcule e mostre a potência do primeiro número
# pelo segundo (X elevado a Y).

base = int(input("Digite o primeiro número inteiro (base): "))
expoente = int(input("Digite o segundo número inteiro (expoente): "))

resultado = base**expoente

print(f"{base} elevado a {expoente} é igual a {resultado}")
