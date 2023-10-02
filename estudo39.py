# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar / se é a hora de se alistar / Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

anoNascimento = int(input('Informe o seu ano de nascimento: '))

anoAtual = 2023

idade = anoAtual - anoNascimento

if idade < 18:
    diferenca = 18 - idade
    if diferenca == 1:
        print('Ainda falta {} ano para se alistar'.format(diferenca))
    else:
        print('Ainda faltam {} anos para se alistar'.format(diferenca))
elif idade == 18:
    print('Está na hora de se alistar')
else:
    diferenca = idade - 18
    if diferenca == 1:
        print('Já passou {} ano para se alistar'.format(diferenca))
    else:
        print('Já passaram {} anos para se alistar'.format(diferenca))