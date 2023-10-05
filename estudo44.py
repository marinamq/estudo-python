# Elabore um programa que calcule o valor a ser pago por um produto, consideranto o seu PREÇO NORMAL e a CONDIÇÃO DE PAGAMENTO
# a vista dinheiro/cheque: -10%
# a vista no cartao: -5%
# até 2x no cartao: preço normal
# 3x ou mais no cartao: +20%

preco_normal = float(input('Digite o preço do produto: '))

print('''Qual a condição de pagamento')
1 - a vista dinheiro/cheque'
2 - a vista no cartão'
3 - em até 2x no cartão'
4 - 3x ou mais no cartão''')

print('----' * 10)

forma_pagamento = int(input('Digite a opção desejada: '))

if forma_pagamento == 1:
    preco_final = preco_normal * 0.9
    print('O valor a ser pago é R$ {:.2f}'.format(preco_final))
elif forma_pagamento == 2:
    preco_final = preco_normal * 0.95
    print('O valor a ser pago é R$ {:.2f}'.format(preco_final))
elif forma_pagamento == 3:
    preco_final = preco_normal
    print('O valor a ser pago é R$ {:.2f}'.format(preco_final))
elif forma_pagamento == 4:
    preco_final = preco_normal * 1.2
    print('O valor a ser pago é R$ {:.2f}'.format(preco_final))
else:
    print('Opção inválida')