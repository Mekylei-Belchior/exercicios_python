"""
 Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
 Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

"""

from random import randint
from time import sleep


def maior(numeros):
    print('-' * 80)
    mValor = max(numeros)

    print('Analisando os valores passados...')

    for n in numeros:
        print(f'{n}', end=' ')
        sleep(0.5)

    print(f'Foram informado(s) {len(numeros)} valores ao todo.')
    print()
    print(f'O maior valor informado foi {mValor}.')
    print('-' * 80)
    sleep(1)


valores = []
numero = []
# tm = randint(1, 10)

for i in range(0, 5):

    tm = randint(1, 10)
    numero.clear()

    for j in range(0, tm):
        numero.append(randint(0, 50))

    valores.append(numero[:])

for i in range(0, len(valores)):
    maior(valores[i])
