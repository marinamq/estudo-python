# Faça um programa qe tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável
# Ex: escreva('Olá, Mundo!)
# saída: __________
#        Olá, Mundo
#        __________

def escreva(texto):
    tam = len(texto)
    print('~'*tam)
    print(texto)
    print('~'*tam)

escreva('Marina Lindona')
escreva('Lucas seu pestinha')
