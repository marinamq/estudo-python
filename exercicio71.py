# Crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunte ao usuário qual será o valor a ser sacado (numero inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# Obs. Considere que o caixa possui cédulas de 50, 20, 10 e 1 real.

saque = int(input("Qual o valor a ser sacado: "))

# if saque >= 50:
#     nota50 = saque // 50
#     nota20 = (saque % 50) // 20
#     nota10 = ((saque % 50) % 20) // 10
#     nota1 = ((saque % 50) % 20) % 10
#     print(f"Você vai receber {nota50} notas de R$ 50.00")
#     print(f"Você vai receber {nota20} notas de R$ 20.00")
#     print(f"Você vai receber {nota10} notas de R$ 10.00")
#     print(f"Você vai receber {nota1} notas de R$ 1.00")
# elif 50 > saque >= 20:
#     nota20 = saque // 20
#     nota10 = (saque % 20) // 10
#     nota1 = ((saque % 20) % 10) // 1
#     print(f"Você vai receber {nota20} notas de R$ 20.00")
#     print(f"Você vai receber {nota10} notas de R$ 10.00")
#     print(f"Você vai receber {nota1} notas de R$ 1.00")
# elif 20 > saque >= 10:
#     nota10 = saque // 10
#     nota1 = saque % 10
#     print(f"Você vai receber {nota10} notas de R$ 10.00")
#     print(f"Você vai receber {nota1} notas de R$ 1.00")
# else:
#     nota1 = saque
#     print(f"Você vai receber {nota1} notas de R$ 1.00")

total = saque
ced = 50
total_ced = 0

while True:
    if total >= ced:
        total -= ced
        total_ced += 1
    else:
        print(f"Total de {total_ced} cedulas de R$ {ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_ced = 0
        if total == 0:
            break
