"""

 Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização
 de detalhes do aproveitamento de cada jogador.

"""

jogador = {}
jogadores = []
gols = []

while True:

    jogador.clear()

    jogador['Nome'] = str(input('Nome: '))

    while True:

        p = input(f'\nQuantas partidas o {jogador["Nome"]} jogou? ')

        if p.isnumeric():
            break

        print(f'\033[1;31mAtenção...\033[m\033[1;36mInforme um número maior ou igual à 0\033[m!')

    partidas = int(p)

    gols.clear()

    for i in range(0, partidas):

        while True:

            gol = input(f'    Quantos gols na partida {i + 1}? ')

            if gol.isnumeric():
                break

            print(f'\033[1;31mAtenção...\033[m\033[1;36mInforme um número maior ou igual à 0\033[m!')

        gols.append(int(gol))
        jogador['Gols'] = gols[:]
        jogador['Total'] = sum(gols)

    jogadores.append(jogador.copy())

    while True:

        resp = str(input('\nDeseja continuar (S/N): ')).strip().upper()[0]

        if resp in 'SN':
            break

        print(f'\033[1;31mAtenção...\033[mDigite um valor válido! \033[1;36m(S - Sim | N - Não)\033[m\n')

    if resp == 'N':
        break

print('\n')
print(f'{"Cod":<7}', end='')

for k in jogador.keys():
    print(f'{k:<30}', end='')

print()
print('-'*75)


for pos, j in enumerate(jogadores):

    print(f'{pos:<7}', end='')

    for v in j.values():

        print(f'{str(v):<30}', end='')

    print()

print('-'*75)

while True:

    while True:

        cod = input('Mostrar os dados de qual jogador? (999 - Finalizar): ')

        if cod.isnumeric():

            cod = int(cod)

            if 0 <= cod <= len(jogadores) - 1 or cod == 999:
                break

            print(f'\033[1;31mNão existe jogador com o código {cod}. TENTE NOVAMENTE!\033[m')

        else:

            print(f'\033[1;31mNão existe jogador com o código {cod}. TENTE NOVAMENTE!\033[m')

    if cod == 999:
        print('\n\033[1;33mPrograma FINALIZADO!!!\033[m')
        break

    print(f'{"-- LEVANTAMENTO DO JOGADOR "} {jogadores[cod]["Nome"]}:')

    for pos, v in enumerate(jogadores[cod]['Gols']):

        print(f'    No jogo {pos + 1} fez {v} gol(s).')
