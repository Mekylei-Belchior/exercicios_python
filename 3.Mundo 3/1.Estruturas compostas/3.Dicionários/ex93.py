"""
 Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
 e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
 será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

"""

jogador = {}
gols = []
p = 1

jogador['Nome'] = str(input('Nome: '))
partidas = int(input(f'\nQuantas partidas o {jogador["Nome"]} jogou? '))

for i in range(0, partidas):

    gols.append(int(input(f'    Quantos gols na partida {i + 1}? ')))
    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)

print()
print('-'*80)
print(jogador)
print('-'*80, '\n')

print('-'*80)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('-'*80, '\n')

print('-'*80)

print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas.')

for p, gol in enumerate(jogador['Gols']):
    print(f'    => Na parida {p + 1}, fez {gol} gol(s).')

print(f'O Jogador fez um total de {jogador["Total"]} gol(s).')
print('-'*80)
