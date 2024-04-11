# Elabore um algoritmo para efetuar o cálculo da quantidade de
# combustível gasto em uma viagem, utilizando-se um automóvel
# que faz 12 Kms por litro. Para obter o cálculo, o usuário deverá fornecer o
# tempo gasto e a velocidade média durante a viagem. Desta forma,
# será possível obter a distância percorrida (distância = tempo * velocidade).

tempo_gasto = float(input("Digite o tempo gasto na viagem (em horas): "))
velocidade_media = float(
    input("Digite a velocidade média durante a viagem (em km/h): ")
)

distancia_percorrida = tempo_gasto * velocidade_media

consumo_por_litro = 12
quantidade_combustivel = distancia_percorrida / consumo_por_litro


print("\nResultado:")
print(
    f"A quantidade de combustível gasto na viagem é de {quantidade_combustivel:.2f} litros."
)
