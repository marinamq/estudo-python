# Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. No final do programa mostre:
# A média de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres tem menos de 20 anos
soma_idade = 0
mais_velho = 0
cont_mulher = 0
nome_mais_velho = ""

for i in range(1, 5):
    nome = str(input("Digite o seu nome: "))
    idade = int(input("Digite a sua idade: "))
    soma_idade += idade

    print(
        """Inform o seu sexo:
    1 - Masculino
    2 - Feminino"""
    )

    sexo = int(input("Digite a opção referente ao seu sexo: "))
    if sexo == 1:
        if idade > mais_velho:
            mais_velho = idade
            nome_mais_velho = nome
    if sexo == 2:
        if idade < 20:
            cont_mulher += 1

media_idade = soma_idade / 4

print(f"A média de idade do grupo é de {media_idade:.2f} anos.")
print(f"O homem mais velho tem {mais_velho} anos e se chama {nome_mais_velho}.")
print(f"{cont_mulher} mulheres tem menos que 20 anos.")
