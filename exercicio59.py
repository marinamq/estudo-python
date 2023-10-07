# Crie um programa que leia dois valores e mostre um menu na tela
# 1 - somar
# 2 - multiplicar
# 3 - maior
# 4 - novos números
# 5 - sair do programa

# Seu programa deverá realizar a operação soliciada em cada caso.

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

opcao = 0

while opcao != 5:

    print('''Selecione a opção desejada:
    1 - somar
    2 - multiplicar
    3 - maior
    4 - novos números
    5 - sair do programa''')

    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        soma = valor1 + valor2
        print('A soma dos valores é {}'.format(soma))
    elif opcao == 2:
        multiplicacao = valor1 * valor2
        print('A multiplicação dos valores é {}'.format(multiplicacao))
    elif opcao == 3:
        if valor1 > valor2:
            print('O maior número é {}'.format(valor1))
        else:
            print('O maior número é {}'.format(valor2))
    elif opcao == 4:
        print('Digite os novos valores!')
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Até logo')
    else:
        print('Opção inválida')
