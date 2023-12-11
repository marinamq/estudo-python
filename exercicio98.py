# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens através da função criada
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")

    sleep(1)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(
                f"{cont} ", end="", flush=True
            )  # precisa usar esse flush=True pra não ter o buffer
            sleep(0.5)
            cont += passo
        print("FIM!")
    else:
        cont = inicio
        while cont >= fim:
            print(f"{cont} ", end="", flush=True)
            sleep(0.5)
            cont -= passo
        print("FIM!")


def mostrarLinha():
    print("-=" * 20)

mostrarLinha()
contador(1, 10, 1)
mostrarLinha()
contador(10, 0, 2)
print("Agora é a sua vez de personalizar a contagem")
ini = int(input("Início: "))
fin = int(input("Fim: "))
pas = int(input("Passo: "))
mostrarLinha()
contador(ini, fin, pas)
