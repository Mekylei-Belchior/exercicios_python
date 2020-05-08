"""
 Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
 O programa vai perguntar quantos jogos serão gerados e vai sortear 6
 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

"""

from random import randint
from time import sleep

print('-'*50)
print(f'{" JOGOS DA MEGA SENA ":^50}')
print('-'*50)

jogos = []
sorteio = []

j = int(input('Deseja gerar quantos jogos? '))

for i in range(0, j):

    while len(sorteio) < 6:

        n = randint(1, 60)

        if n not in sorteio:
            sorteio.append(n)

    jogos.append(sorteio[:])
    sorteio.clear()

print()

for i in range(0, len(jogos)):
    print('GERANDO O JOGO', end='')

    for j in range(0, 4):
        sleep(0.5)
        print('.', end='')

    print('OK', end='')
    print()

    print(f'Jogo {i + 1}: {sorted(jogos[i])}')
    print()
