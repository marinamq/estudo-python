# Crie um prgrama que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere US$ 1.00 = R$ 3.27

n = float(input('Digite o quanto de dinheiro você tem na carteira: '))

compra_dolar = n / 3.27

print('Você consegue comprar {} dólares.'.format(compra_dolar))