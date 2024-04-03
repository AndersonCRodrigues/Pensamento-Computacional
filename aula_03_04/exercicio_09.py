"""
Faça um algoritmo que após a entrada de uma determinada distância entre dois
pontos(Km), e uma determinada velocidade(Km/h), diga qual o tempo médio que
levará para chegada à esse local e qual a velocidade em metros/segundos.
"""

velocidade = int(input("Entre com a velocidade em km/h: "))
distancia = int(input("Entre com a distancia em km: "))

tempo = distancia / velocidade

print(
    f"Para percorrer {distancia} km a {velocidade} km/h, "
    f"irá demorar {tempo} horas "
)
