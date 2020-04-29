"""
 Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
 O programa será interrompido quando o número solicitado for negativo.

"""

print('-'*100)
print(f'{"TABUADA":^100}')
print('-'*100)

while True:

    n = int(input('\nDeseja ver a tabuada de qual número? '))

    if n > 0:

        print(f'TABUADA DE {n}: ')

        for i in range(1, 11):

            print(f'{n} x {i} = {i * n}')
        print('-' * 100)

    else:
        break

print('Programa finalizado!')
