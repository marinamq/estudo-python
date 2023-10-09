# Refaça o desafio 35 dos triângulos acrescentando o recurso de mostrar que tipo de triânglo será formado:
# Equilatero: topdos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

reta1 = int(input("Digite o tamanho da primeira reta: "))
reta2 = int(input("Digite o tamanho da segunda reta: "))
reta3 = int(input("Digite o tamanho da terceira reta: "))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    if reta1 == reta2 and reta1 == reta3 and reta2 and reta3:
        print("Forma um triângulo equilátero")
    elif reta1 != reta2 and reta1 != reta3 and reta2 != reta3:
        print("Forma um triângulo escaleno")
    else:
        print("Forma um triângulo isósceles")
else:
    print("não forma triangulo")
