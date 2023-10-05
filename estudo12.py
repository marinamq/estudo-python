# Faça um algorítmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input('Digite o preço do produto: '))

preco_desconto = preco * 0.95

print('O preço com desconto de 5% é de {}.'.format(preco_desconto))