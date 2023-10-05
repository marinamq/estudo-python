# Faça um progrma que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 até 500

for num in range(1, 501):
    if num % 3 == 0 and num % 2 !=0:
        num += num
        print(num)