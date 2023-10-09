# Crie um programa que leia o nome de uma cidade e gida se ela começa ou não com o nome "Santo"

cidade = str(input("Digite o nome da cidade: ")).strip()

cidade1 = cidade.split()

cidade2 = cidade1[0]
cidade2 = cidade2.lower()

checagem = "santo" in cidade2

if checagem == True:
    print("O nome da cidade começa com Santo")
else:
    print("O nome da cidade não começa com Santo")
