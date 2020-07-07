"""
 Crie um programa que simule o funcionamento de um caixa eletrônico.
 No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
 e o programa vai informar quantas cédulas de cada valor serão entregues.

 OBS: considere que o caixa possui cédulas de R$100, R$50, R$20, R$10, R$5, R$2 e R$1.

"""

print('='*50)
print(f'{"BANCO DA MÃE JOANA":^50}')
print('='*50)

c1 = c2 = c5 = c10 = c20 = c50 = c100 = 0

total = saque = int(input('\nQual o valor que você deseja sacar? '))

while True:

    if total != 0:

        if total // 100 > 0:
            c100 = total // 100
            total -= c100 * 100

        if total // 50 > 0:
            c50 = total // 50
            total -= c50 * 50

        elif total // 20 > 0:
            c20 = total // 20
            total -= c20 * 20

        elif total // 10 > 0:
            c10 = total // 10
            total -= c10 * 10

        elif total // 5 > 0:
            c5 = total // 5
            total -= c5 * 5

        elif total // 2 > 0:
            c2 = total // 2
            total -= c2 * 2

        elif total // 1 > 0:
            c1 = total // 1
            total -= c1 * 1

    else:

        break

print('\n')
if c100 > 0:
    print(f'Total de cédulas de R$ 100,00 = {c100}')

if c50 > 0:
    print(f'Total de cédulas de R$ 50,00 = {c50}')

if c20 > 0:
    print(f'Total de cédulas de R$ 20,00 = {c20}')

if c10 > 0:
    print(f'Total de cédulas de R$ 10,00 = {c10}')

if c5 > 0:
    print(f'Total de cédulas de R$ 5,00 = {c5}')

if c2 > 0:
    print(f'Total de cédulas de R$ 2,00 = {c2}')

if c1 > 0:
    print(f'Total de cédulas de R$ 1,00 = {c1}')

print(f'\n\033[1;36m{"Saque realizado com sucesso!":^50}\033[m')




