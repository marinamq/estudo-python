# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

# sexo = ''
sexo = str((input("Informe o seu sexo:[M/F] "))).upper()[0].strip()


while sexo not in "MFmf":
    sexo = str(input("Dados inválidos. Informe o seu sexo: ")).upper()[0].strip()
print(f"Sexo {sexo} registrado com sucesso")
