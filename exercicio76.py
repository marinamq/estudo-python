# Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços na sequencia
# no final, mostre uma listagem de preços, organizando os dados em forma tabular.

listagem = (
    "caderno",
    15.5,
    "borracha",
    1.50,
    "caneta",
    0.80,
    "mochila",
    20,
    "estojo",
    10,
)

print("-" * 35)
print(" " * 7, "LISTAGEM DE PREÇOS")
print("-" * 35)

print(f"{listagem[0]}", "." * 18, "R$ ", f"{listagem[1]:.2f}")
print(f"{listagem[2]}", "." * 17, "R$ ", f"{listagem[3]:.2f}")
print(f"{listagem[4]}", "." * 19, "R$ ", f"{listagem[5]:.2f}")
print(f"{listagem[6]}", "." * 18, "R$ ", f"{listagem[7]:.2f}")
print("-" * 35)


# resolução do guanabara
print("-" * 40)
print(f"{'LISTAGEM DE PREÇOS':^40}")
print("-" * 40)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}", end="")
    else:
        print(f"R${listagem[pos]:>7.2f}")
print("-" * 40)
