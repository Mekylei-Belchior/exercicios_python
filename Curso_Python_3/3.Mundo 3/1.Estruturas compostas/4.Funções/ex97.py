"""
 Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre
 uma mensagem com tamanho adaptável.

"""

def escreva(msg):

    print('-' * len(msg))
    print(msg)
    print('-' * len(msg))


frase = 'Olá, mundo!'
texto = 'Curso de Python 3. Aprendendo a programar em uma linguagem simples e poderosa.'
vogais = 'a, e, i, o, u'

escreva(frase)
escreva(texto)
escreva(vogais)
