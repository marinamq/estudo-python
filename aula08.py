# dessa forma importa todas as funcionalidades
import math

# para importar um método específico, é feito dessa forma:
# from math import sqrt // e para chamar a função faz assim: raiz = sqrt(num) // Não precisa escrever o "math."sqrt
# caso queira importar mais de um método, é assim que faz:
# from math import sqrt, ceil

num = int(input('Digite um número: '))

raiz = math.sqrt(num)

print('A raiz de {} é igual a {}'.format(num, raiz))

#sqrt -> calcula a raíz
#ceil -> arredonda para cima
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
#floor -> arredonda para baixo
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))
