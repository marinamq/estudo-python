# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido qando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

import random

print('=-'*15)
print("VAMOS JOGAR PAR OU ÍMPAR")
print('=-'*15)
cont = 0

while True:
    num_jogador = int(input("Diga um valor: "))
    opcao = str(input("Par ou Ímpar? [P/I] ")).upper().strip()[0]
    print('-'*30)
    num_pc = random.randint(0, 10)
    soma = num_jogador + num_pc

    if soma % 2 == 0:
        if opcao == 'P':
            print(
                f'Você jogou {num_jogador} e o computador {num_pc}. Total de {soma} deu PAR')
            print('-'*30)
            print('Você venceu')
            print('Vamos jogar novamente...')
            print('=-'*15)
            cont += 1
        if opcao == 'I':
            print(
                f'Você jogou {num_jogador} e o computador {num_pc}. Total de {soma} deu PAR')
            print('-'*30)
            print('Você perdeu')
            print('=-'*15)
            break
    if soma % 2 != 0:
        if opcao == 'P':
            print(
                f'Você jogou {num_jogador} e o computador {num_pc}. Total de {soma} deu ÍMPAR')
            print('-'*30)
            print('Você perdeu')
            print('=-'*15)
            break
        if opcao == 'I':
            print(
                f'Você jogou {num_jogador} e o computador {num_pc}. Total de {soma} deu ÍMPAR')
            print('Você venceu')
            print('Vamos jogar novamente...')
            print('=-'*15)
            print('-'*30)
            cont += 1

print(f'GAME OVER! Você venceu {cont} vezes')
