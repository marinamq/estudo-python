# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
# se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos;
# B) Quantos homens foram cadastrados
# c) Quantas mulheres tem menos de 20 anos

option = "S"
cont_age = cont_sex_male = cont_sex_female = 0

while option == "S":
    print("-" * 30)
    print(" " * 5, "CADASTRE UMA PESSOA")
    print("-" * 30)
    age = int(input("Idade: "))
    if age > 18:
        cont_age += 1
    sex = str(input("Sexo [M/F]: ")).upper().strip()[0]
    while sex not in ("M", "F"):
        sex = str(input("Sexo [M/F]: ")).upper().strip()[0]
    if sex == "M":
        cont_sex_male += 1
    if sex == "F":
        if age < 20:
            cont_sex_female += 1
    option = str(input("Quer continuar [S/N]: ")).upper().strip()[0]
    while option not in ("S", "N"):
        option = str(input("Quer continuar [S/N]: ")).upper().strip()[0]

print("=" * 5, "FIM DO PROGRAMA", "=" * 5)
print(f"{cont_age} pessoas têm mais de 18 anos.")
print(f"{cont_sex_male} homens foram cadastrados.")
print(f"{cont_sex_female} mulheres tem menos de 20 anos.")
