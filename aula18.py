# LISTAS DENTROS DE LISTAS

# dados = []
# dados.append("Pedro")
# dados.append(25)
# dados.append("Maria")
# dados.append(22)
# dados.append("Joao")
# dados.append(32)
# print(dados[0])
# print(dados[1])

# pessoas = []
# pessoas.append(dados[:])
# print(pessoas)
# pessoas = [["PEDRO", 25], ["MARIA", 22], ["JOAO", 32]]
# print(pessoas[0])
# print(pessoas[0][0])
# print(pessoas[1][1])
# print(pessoas[2][0])
# print(pessoas[1])
# pessoas.clear() #vai deletar os valores das duas listas, dados e pessoas
print("=-" * 60)

galera = []
dado = []
totmai = totmen = 0

for c in range(0, 3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade")
        totmai += 1
    else:
        print(f"{p[0]} é menor de idade")
        totmen += 1
print(f"Temos {totmai} maiores e {totmen} menores de idade.")