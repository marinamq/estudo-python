# Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiam a maioridade e quantas já são maiores.
from datetime import date

ano_atual = date.today().year
total_maior = 0
total_menor = 0

for i in range(1, 8):
    ano_nascimento = int(input('Digite o ano de nascimento: '))
    idade = ano_atual - ano_nascimento
    if idade < 18:
        total_menor += 1
    else:
        total_maior += 1
print('{} pessoas menores de idade'.format(total_menor))
print('{} pessoas maiores de idade'.format(total_maior))