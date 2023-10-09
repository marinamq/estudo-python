# A confederação nacional de natação  precisa de um programa que leia o ano de nascimento de um atleta e mostre sua caegoria, de acordo com a idade
# até 9 anos: mirim
# até 14 anos: infantil
# até 19 anos : jnior
# até 25 anos : senior
# acima: master

from datetime import date

ano_nascimento = int(input("Digite o ano do seu nascimento: "))

ano_atual = date.today().year

idade = ano_atual - ano_nascimento

if idade <= 9:
    print("Categoria Mirim")
elif idade <= 14:
    print("Categoria Infantil")
elif idade <= 19:
    print("Categoria Júnior")
elif idade <= 25:
    print("Categoria Sênior")
else:
    print("Categoria Master")
