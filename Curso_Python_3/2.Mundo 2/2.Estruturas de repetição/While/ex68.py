"""
 Faça um programa que jogue par ou ímpar com o computador.
 O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que
 ele conquistou no final do jogo.

"""

from random import randint

cont = soma = 0

while True:

    pc = randint(1, 5)
    n = 0
    r = 'a'

    while n not in range(1, 6):

        n = int(input('\nInforme o seu número (1 - 5): '))

    while r not in 'IP':

        r = str(input('Escolha PAR ou ÍMPAR: ')).strip().upper()[0]

    soma = pc + n

    if r in 'IÍ':

        if soma % 2 == 1:
            print(f'\n\nO computador jogou ({pc}) e pediu PAR. Você jogou ({n}) e pediu ÍMPAR. VOCÊ VENCEU!')
            cont += 1

        else:
            print(f'O computador jogou ({pc}) e pediu PAR. Você jogou ({n}) e pediu ÍMPAR. VOCÊ PERDEU!')
            break

    if r == 'P':

        if soma % 2 == 0:
            print(f'\n\nO computador jogou ({pc}) e pediu ÍMPAR. Você jogou ({n}) e pediu PAR. VOCÊ VENCEU!')
            cont += 1

        else:
            print(f'O computador jogou ({pc}) e pediu ÍMPAR. Você jogou ({n}) e pediu PAR. VOCÊ PERDEU!')
            break

print(f'\n\n\033[1;36mVocê venceu ({cont}) partida(s) consecutiva(s).\033[m')
