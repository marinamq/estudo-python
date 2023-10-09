# Melhore o jogo DESAFIO 28 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora
# o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer


import random

numero = random.randint(0, 11)

tentativa_usuario = int(input("Tente adivinhar o número escolhido de 0 a 10: "))

cont_palpite = 0

while tentativa_usuario != numero:
    cont_palpite += 1
    tentativa_usuario = int(input("Tente adivinhar o número escolhido de 0 a 10: "))

print(f"O numero escolhido é {numero} e você digitou {tentativa_usuario}")
print(f"Você precisou de {cont_palpite + 1} tentativas para acertar")
