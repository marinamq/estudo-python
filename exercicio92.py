# Crie um programa que leia, nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
# Se por acaso a CPTS for diferente de zero, o dicionário receberpa também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime


dados = {}

dados["nome"] = str(input("Digite o seu nome: "))
nascimento = int(input("Digite o ano de nascimento: "))

dados["idade"] = datetime.now().year - nascimento
dados["ctps"] = int(input("Digite a carteira de trabalho (0 não tem): "))

if dados["ctps"] != 0:
    dados["contratacao"] = int(input("Digite o ano de contratação: "))
    dados["salario"] = float(input("Digit eo seu salário: R$ "))
    dados["aposentadoria"] = dados["idade"] + (
        (dados["contratacao"] + 35) - datetime.now().year
    )

print("-=" * 30)

for k, v in dados.items():
    print(f"{k} tem o valor {v}")
