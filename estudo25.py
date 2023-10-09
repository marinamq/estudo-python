# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome

nome = str(input("Digite o seu nome: ")).strip()

nome = nome.lower()

checagem = "silva" in nome

if checagem == True:
    print("Você possui Silva no seu nome.")
else:
    print("Você não possui Silva no seu nome.")
