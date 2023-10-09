# Crie um programa que tenha uma tupla com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação.
# Depois mostre:
# Apenas os 5 primeiros colocados
# os ultimos 4 colocados da tabela
# uma lista em ordem alfabetica
# em que posicao na tabela está o time da chapecoense

tabela = (
    "botafogo",
    "bragantino",
    "gremio",
    "palmeira",
    "flamengo",
    "fluminense", 
    "atletico-mg",
    "atletico-pr",
    "fortaleza",
    "sao paulo",
    "cuiaba",
    "corinthians",
    "cruzeiro",
    "internacional",
    "bahia",
    "vasco da gama",
    "santos",
    "goiás",
    "america-mg",
    "coritiba",
)

print(tabela[:5])
print(tabela[-4:])
print(sorted(tabela))
print(tabela.index("corinthians")+1)
