"""

 Crie um programa que leia um número real qualquer e mostre na tela a sua porção inteira.

"""

from math import trunc

num = float(input('Digite um número: '))

print(f'A porção inteira do número {num} é: {trunc(num)}')
