"""
 Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
 No final, mostre a matriz na tela, com a formatação correta.

"""

matriz = [[], [], []]

for i in range(0, 3):

    for j in range(0, 3):

        n = int(input(f'Digite um valor para ({i}, {j}): '))
        matriz[i].append(n)

print()

for i in range(0, 3):

    for j in range(0, 3):
        print(f'[{matriz[i][j]:^6}]', end='')

    print()
