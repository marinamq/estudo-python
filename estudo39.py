# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar / se é a hora de se alistar / Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano_nascimento = int(input("Informe o seu ano de nascimento: "))

anoAtual = date.today().year

idade = anoAtual - ano_nascimento

if idade < 18:
    diferenca = 18 - idade
    if diferenca == 1:
        print(f"Ainda falta {diferenca} ano para se alistar")
    else:
        print(f"Ainda faltam {diferenca} anos para se alistar")
elif idade == 18:
    print("Está na hora de se alistar")
else:
    diferenca = idade - 18
    if diferenca == 1:
        print(f"Já passou {diferenca} ano para se alistar")
    else:
        print(f"Já passaram {diferenca} anos para se alistar")
