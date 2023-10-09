# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas minúsculas
# Quantas letras tem ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = str(input("Digite o seu nome completo: ")).strip()

print(nome.upper())

print(nome.lower())

nome1 = nome.split()
nome2 = "".join(nome1)
print(len(nome2))

print(len(nome1[0]))
