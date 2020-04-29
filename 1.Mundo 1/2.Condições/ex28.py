"""
 Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

 O programa deverá escrever na tela se o usuário ganhou ou perdeu.

"""

from random import randint
from time import sleep

print('\033[1;31m*-*\033[m' * 20)
print('Foi sorteado um número de 0 à 5. Tente adivinhar o número...')
print('\033[1;31m*-*\033[m' * 20)

n = randint(0, 5)

num = int(input('Qual é o número? '))

print('\n\033[0;36mVERIFICANDO...\033[m')
sleep(2)

print('\nVocê \033[1;32mACERTOU\033[m!'if num == n else f'\nVocê \033[1;31mERROU\033[m! O número correto é: {n}')

"""
if num == n:
    print('Você acertou!')
else:
    print(f'Você errou! O Número correto é: {n}')
"""