"""
 Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
 Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

"""

from random import sample

"""
tupla = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

"""

tupla = tuple(sample(range(0, 101), 5))

print(f'Números sorteados: {tupla}')
print(f'\nO menor valor é ({min(tupla)}) e o maior valor é ({max(tupla)})')

