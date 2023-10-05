# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar O VALOR DA CASA, O SALARIO do comprador e em QUANTOS ANOS ele vai pagar.
# Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negado.

valor_casa = float(input('Informe o valor da casa: '))
salario = float(input('Informe o seu salário: '))
tempo = int(input('Informe em quantos anos irá pagar o empréstimo: '))

parcela = (valor_casa / tempo) / 12


if parcela > (salario * 0.3):
    print('Empréstimo negado')
else:
    print('Empréstimo aprovado')
    print('Parcela mensal de RS {:.2f}'.format(parcela))