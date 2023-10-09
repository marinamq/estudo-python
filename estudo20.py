import random

aluno1 = str(input("Digite o nome do aluno: "))
aluno2 = str(input("Digite o nome do aluno: "))
aluno3 = str(input("Digite o nome do aluno: "))
aluno4 = str(input("Digite o nome do aluno: "))

lista = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(lista)

print(f"A ordem da apresentação é {lista}.")
