# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno  = {}

aluno["nome"] = str(input("Digite o nome do aluno: "))
aluno["media"] = float(input(f"Média de {aluno['nome']}: "))
if aluno["media"] >= 7:
    aluno["situacao"] = "Aprovado"
elif 5 <= aluno["media"] < 7:
    aluno["situacao"] = "Recuperação"
else:
    aluno["situacao"] = "Reprovado"

print("-=" * 30)

for k, v in aluno.items():
    print(f"{k} = {v}")
print("-=" * 30)
