# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# Quantas pessoas foram cadastradas
# A média de idade do grupo
# Uma lista com todas as mulheres
# Uma lista com todas as pessoas com idadde acima da média

dados = {}
lista_dados = []
soma = media = 0

while True:
    dados.clear()
    dados["nome"] = str(input("Nome: "))
    while True:
        dados["sexo"] = str(input("Sexo: [M/F] ")).upper().strip()[0]
        if dados["sexo"] in "MF":
            break
        print("Erro! Por favor digite apenas M ou F")
    dados["idade"] = int(input("Idade: "))
    soma += dados["idade"]
    lista_dados.append(dados.copy())
    while True:
        resp = str(input("Deseja cadastrar outra pessoa: [S/N]")).upper().strip()[0]
        if resp in "SN":
            break
        print("Erro! Por favor digite apenas S ou N")
    if resp == "N":
        break

print(f"Temos {len(lista_dados)} pessoas cadastradas")

media = soma / len(lista_dados)

print(f"A média de idade é {media:5.2f} anos.")

print("As mulheres cadastradas foram: ", end="")
for p in lista_dados:
    if p["sexo"] in "fF":
        print(f"{p['nome']} ", end="")
print()

print("Lista das pessoas que estão com idade acima da média: ", end="")
for p in lista_dados:
    if p["idade"] > media:
        print(f"{p['nome']} ", end="")
