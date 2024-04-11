# Um hotel deseja fazer uma promoção especial de final de semana,
# concedendo um desconto de 25% na diária. Sendo informados,
# através do teclado, o número de apartamentos do hotel e o valor
# da diária por apartamento para o final de semana completo,
# elabore um programa para calcular:

# a. Valor promocional da diária;

# b. Valor total a ser arrecadado caso a ocupação neste
# final de semana atinja 100%;

# c. Valor total a ser arrecadado caso a ocupação neste
# final de semana atinja 70%;

# d. Valor que o hotel deixará de arrecadar em virtude da promoção,
# caso a ocupação atinja 100%.

num_apartamentos = int(input("Digite o número de apartamentos do hotel: "))
valor_diaria = float(input("Digite o valor da diária por apartamento: "))

desconto = 0.25
valor_promocional = valor_diaria * (1 - desconto)

total_100 = num_apartamentos * valor_promocional

ocupacao_70 = 0.7
total_70 = num_apartamentos * valor_promocional * ocupacao_70

perda_promocao = (num_apartamentos * valor_diaria) - total_100

print("\nResultados:")
print(f"Valor promocional da diária: R${valor_promocional:.2f}")
print(f"Valor total a ser arrecadado com 100% de ocupação: R${total_100:.2f}")
print(f"Valor total a ser arrecadado com 70% de ocupação: R${total_70:.2f}")
print(
    f"Valor que o hotel deixará de arrecadar em virtude da promoção:"
    f"R${perda_promocao:.2f}"
)
