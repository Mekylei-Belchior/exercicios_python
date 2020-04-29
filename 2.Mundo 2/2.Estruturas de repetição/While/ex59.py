"""
 Crie um programa que leia dois valores e mostre um menu na tela:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
 Seu programa deverá realizar a operação solicitada em cada caso.

"""
from time import sleep

print(f'{" CALCULADORA ":#^60}\n\n')

num1 = float(input('Digite o 1º valor: '))
num2 = float(input('Digite o 2º valor: '))

op = 0

while op != 5:

    op = int(input("""\nEscolha uma opção:\n
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa\n"""))

    if op == 1:
        print(f'\n\033[1;31mA soma dos valores ({num1} + {num2}) é:\033[m {num1 + num2}\n')

    elif op == 2:
        print(f'\n\033[1;31mA multiplicação dos valores ({num1} * {num2}) é:\033[m {num1 * num2}\n')

    elif op == 3:
        print(f'\n\033[1;31mO maior valor de ({num1} e {num2}) é:\033[m {num1 if num1 > num2 else num2}\n')

    elif op == 4:
        num1 = float(input('Digite o 1º valor: '))
        num2 = float(input('Digite o 2º valor: '))

    elif op == 5:
        print('Encerrando...')
        sleep(2)
        print('Fim....')

    else:
        print('Opção inválida. Tente novamente!')
