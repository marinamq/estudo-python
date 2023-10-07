# Crie um programa que leia o nome e o preço de vários produtos. O programa devrá perguntar se o usuário vai continuar. No final mostre:
# Qual é o total gasto na compra
# Quantos produtos custam mais de R$ 1000
# Qual é o nome do produto mais barato


option = "S"

total_spent = product_thousand = product_price = 0
# cheaper_product = product_price = 0

while option == "S":
    print("-" * 30)
    print(" " * 5, "LOJA SUPER BARATÃO")
    print("-" * 30)
    product_name = str(input("Digite o nome do produto: ")).strip()
    product_price = float(input("Digite o preço do produto: R$ "))
    total_spent += product_price
    if product_price > 1000:
        product_thousand += 1
    option = str(input("Deseja continuar [S/N]? ")).upper().strip()[0]

print("=" * 5, "FIM DO PROGRAMA", "=" * 5)
print(f"O total da compra foi R$ {total_spent:.2f}")
print(f"Temos {product_thousand} produtos custando mais de R$ 1000.00")
# print(f"O produto mais barato foi {} que custa {}")
