"""
 Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
 Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que
 o vencedor tirou o maior número no dado.

"""

from random import randint
from time import sleep

jogadores = {}
p = 1

print()

for i in range(0, 4):

    dado = int(randint(1, 6))
    jogadores[i + 1] = dado

for i in range(1, 5):
    print(f'O jogador {i} tirou {jogadores[i]} no dado.')
    sleep(0.8)

print()
print(f'{"*"*10} {" RANK DOS JOGADORES ":^20} {"*"*10}', '\n')

for i in sorted(jogadores, key=jogadores.get, reverse=True):
    print(f'{p}º lugar: Jogador ({i}) com: {jogadores[i]}')

    p += 1
