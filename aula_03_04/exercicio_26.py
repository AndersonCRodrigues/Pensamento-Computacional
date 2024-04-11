# Considerando uma eleição de apenas 2 candidatos, elabore um
# algoritmo que leia do teclado o número total de eleitores,
# o número de votos do primeiro candidato e o número de votos
# do segundo candidato.
# Em seguida, o algoritmo deverá apresentar o percentual de votos
# de cada um dos candidatos e o percentual de votos nulos.

total_eleitores = int(input("Digite o número total de eleitores: "))
votos_candidato1 = int(input("Digite o número de votos do primeiro candidato: "))
votos_candidato2 = int(input("Digite o número de votos do segundo candidato: "))

percentual_candidato1 = (votos_candidato1 / total_eleitores) * 100
percentual_candidato2 = (votos_candidato2 / total_eleitores) * 100

votos_nulos = total_eleitores - (votos_candidato1 + votos_candidato2)
percentual_nulos = (votos_nulos / total_eleitores) * 100

print("\nResultados:")
print(f"Percentual de votos do primeiro candidato: {percentual_candidato1:.2f}%")
print(f"Percentual de votos do segundo candidato: {percentual_candidato2:.2f}%")
print(f"Percentual de votos nulos: {percentual_nulos:.2f}%")
