"""
 Crie um programa que faça o computador jogar Jokenpô com você.

"""
from random import choice
from time import sleep

jk = [0, 2, 5]

pc = choice(jk)

print(f'{" JOGO JOKENPO ":=^40}')

op = int(input(f'\nOPÇÕES:\n\n[0] - Pedra\n[2] - Tesoura\n[5] - Papel'))

print('\nJO\n')
sleep(1)

print('KEN\n')
sleep(1)

print('PO\n')

if pc == 0 and op == 0:
    print('Computador: PEDRA x Você: PEDRA = \033[1;36mEMPATE!')

elif pc == 2 and op == 2:
    print('Computador: TESOURA x Você: TESOURA = \033[1;36mEMPATE!')

elif pc == 5 and op == 5:
    print('Computador: PAPEL x Você: PAPEL = \033[1;36mEMPATE!')

elif pc == 0 and op == 2:
    print('Computador: PEDRA x Você: TESOURA = \033[1;31mCOMPUTADOR GANHOU!')

elif pc == 0 and op == 5:
    print('Computador: PEDRA x Você: PAPEL = \033[1;34mVOCÊ GANHOU!')

elif pc == 2 and op == 0:
    print('Computador: TESOURA x Você: PEDRA = \033[1;34mVOCÊ GANHOU!')

elif pc == 2 and op == 5:
    print('Computador: TESOURA x Você: PAPEL = \033[1;31mCOMPUTADOR GANHOU!')

elif pc == 5 and op == 0:
    print('Computador: PAPEL x Você: PEDRA = \033[1;31mCOMPUTADOR GANHOU!')

elif pc == 5 and op == 2:
    print('Computador: PAPEL x Você: TESOURA = \033[1;34mVOCÊ GANHOU!')

else:
    print('Opção INVÁLIDA! Tente novamente!')