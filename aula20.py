# FUNÇÕES
def mostralinha():
    print("-" * 30)


mostralinha()
print("     SISTEMAS DE ALUNOS        ")
mostralinha()
mostralinha()
print("     CADASTRO DE ALUNOS        ")
mostralinha()
mostralinha()
print("     EXCLUSAO DE ALUNOS        ")
mostralinha()
mostralinha()
print("        NOTAS DE ALUNOS        ")
mostralinha()

# comando personalisando utilizando parametro


def titulo(txt):
    print("-" * 30)
    print(txt)
    print("-" * 30)


titulo("     SISTEMAS         ")

titulo("     CADASTRO         ")

titulo("     EXCLUSAO         ")

titulo("     NOTAS            ")

# AULA PRÁTICA

a = 4
b = 5
s = a + b
print(s)

a = 6
b = 5
s = a + b
print(s)

a = 4
b = 8
s = a + b
print(s)

print("-" * 30)

def soma(a, b):
    print(f"A = {a} e B = {b}")
    s = a + b
    print(f"A soma A + B = {s}")
    print("-"*30)
#Programa principal
soma(4, 5)
soma(6, 5)
soma(4, 8)

# empacotar parâmetros
# def contador (*num): vai gerar uma tupla nesse caso

def contador(*num):
    print(num)
    print("=" * 30)

contador(2, 1, 7)
contador(8, 0)
contador(5, 4, 3, 2, 1)

print("-="*30)

# empacotar parametro com lista

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

valores = [5, 6, 9, 7, 8]

dobra(valores)
print(valores)

print("-="*30)

# desempacotar

def soma1(*valores1):
    s = 0
    for num in valores1:
        s += num
    print(f"Somando os valores {valores1} temos {s}")

soma1(5, 2)
soma1(2, 9, 4)
