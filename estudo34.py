# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salarios superiores a R$ 1.250,00, aumento de 10%
# Para inferiores ou iguais a $1.250,00, aumento é de 15%

salario = float(input('Digite o seu salário: '))

if salario > 1250:
    aumento = salario * 1.10
    print('O novo salário é {:.2f}'.format(aumento))
else:
    aumento = salario * 1.15
    print('O novo salário é {:.2f}'.format(aumento))