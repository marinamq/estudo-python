# DICIONÁRIOS

dados = {}

dados = {"nome": "Pedro", "idade": 25}

print(dados["nome"])
print("=-" * 30)

# para criar novo elemento
dados["sexo"] = "M"
print(dados)
print("=-" * 30)

print(
    f"O {dados['nome']} tem {dados['idade']} anos."
)  # assim que vai tratar o dicionario no print formatado
print(dados.keys())
print(dados.values())
print(dados.items())
print("=-" * 30)

# para remover elemento
del dados["idade"]
print(dados)
print("=-" * 30)
# criar outro dicionário

filme = {"titulo": "Star wars", "ano": 1997, "diretor": "George Lucas"}

print(filme)

# valor, chave e item
print(filme.values())  # retorna todos os valores do dicionário
print(filme.keys())  # retorna as chaves
print(
    filme.items()
)  # pega todos os dados ( valores e keys ). No dicionário usa o items, não tem enumerate

for k, v in filme.items():
    print(f"O {k} é {v}")

for k in filme.keys():
    print(k)
for k in filme.values():
    print(k)

# como criar um dicionário dentro de uma lista
# brasil = []

# estado1 = {"uf": "Rio de Janeiro", "sigla": "RJ"}
# estado2 = {"uf": "São Paulo", "sigla": "SP"}

# brasil.append(estado1)
# brasil.append(estado2)

# print(estado1) # vai mostrar o dicionário estado 1
# print(estado2) # vai mostrar o dicionário estado 2
# print(brasil) # mostra a lista com os 2 dicionários dentro
# print(brasil[0])
# print(brasil[0]["uf"])

print("=-" * 60)

estado = {}
pais = []

for c in range(0, 3):
    estado["uf"] = str(input("Undade Federativa: "))
    estado["sigla"] = str(input("Sigla: "))
    pais.append(estado.copy()) # assim que faz para copiar um conteúdo
print(pais)
print("=-" * 30)
for e in pais:
    for k, v in e.items():
        print(f"O campo {k} tem valor {v}")
# ou
print("=-" * 30)
for e in pais:
    for v in e.values():
        print(v, end=" ")
    print() # pula de linha
