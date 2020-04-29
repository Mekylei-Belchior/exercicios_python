"""
 Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

"""
print(f'{"Números Primos":=^40}\n')

n = int(input('Digite um número: '))
cont = 0

for i in range(1, n + 1):

    if n % i == 0:
        print('\033[1;31m', end=' ')
        cont += 1

    else:
        print('\033[m', end=' ')

    print(i, end=' ')

if cont == 2:
    print(f'\n\033[mO número ({n}) é divisível por ({cont}) números. Ou seja, \033[1;4;36mÉ UM NÚMERO PRIMO'
          f'\033[m.')

else:
    print(f'\n\n\033[mO número ({n}) é divisível por ({cont}) números. Ou seja, \033[1;4;33mNÃO É UM NÚMERO PRIMO'
          f'\033[m.')
