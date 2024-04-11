# Faça um algoritmo que receba o custo de um espetáculo teatral e o preço do
# convite esse espetáculo. Esse programa deve calcular e mostrar:

# a. A quantidade de convites que devem ser vendidos para que pelo menos o
# custo do espetáculo seja alcançado.

# b. A quantidade de convites que devem ser vendidos para que se tenha um
# lucro de 23%.

custo_espetaculo = float(input("Digite o custo do espetáculo teatral: R$ "))
preco_convite = float(input("Digite o preço do convite: R$ "))

convites_para_custo = custo_espetaculo / preco_convite

lucro_percentual = 0.23
convites_para_lucro = custo_espetaculo / (preco_convite * (1 - lucro_percentual))

print("\nResultados:")
print(
    f"Quantidade de convites para cobrir o custo do espetáculo: {int(convites_para_custo)} convites"
)
print(
    f"Quantidade de convites para obter um lucro de 23%: {int(convites_para_lucro)} convites"
)
