"""
 Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
 Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

"""

num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
       'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:

    while True:

        n = int(input('Digite um número de 0 à 20: '))

        if 0 <= n <= 20:
            break

        print('Tente novamente! ', end='')

    print(f'\nVocê digitou: {num[n]}')

    while True:

        r = str(input('\nDeseja continuar (S - Sim e N - Não): ')).strip().upper()[0]

        if r in 'SN':
            print('\n')
            break

    if r == 'N':
        print('PROGRAMA FINALIZADO!')
        break
