# Elabore um programa que calcule o valor a ser pago por um produto, consideranto o seu PREÇO NORMAL e a CONDIÇÃO DE PAGAMENTO
# a vista dinheiro/cheque: -10%
# a vista no cartao: -5%
# até 2x no cartao: preço normal
# 3x ou mais no cartao: +20%

precoNormal = float(input('Digite o preço do produto: '))

print('''Qual a condição de pagamento')
1 - a vista dinheiro/cheque'
2 - a vista no cartão'
3 - em até 2x no cartão'
4 - 3x ou mais no cartão''')

print('----' * 10)

formaPagamento = int(input('Digite a opção desejada: '))

if formaPagamento == 1:
    precoFinal = precoNormal * 0.9
    print('O valor a ser pago é R$ {:.2f}'.format(precoFinal))
elif formaPagamento == 2:
    precoFinal = precoNormal * 0.95
    print('O valor a ser pago é R$ {:.2f}'.format(precoFinal))
elif formaPagamento == 3:
    precoFinal = precoNormal
    print('O valor a ser pago é R$ {:.2f}'.format(precoFinal))
elif formaPagamento == 4:
    precoFinal = precoNormal * 1.2
    print('O valor a ser pago é R$ {:.2f}'.format(precoFinal))
else:
    print('Opção inválida')