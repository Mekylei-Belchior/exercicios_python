"""
 Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número
 a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela
 o processo de cálculo do fatorial.

"""


def fatorial(num, show=True):
    """
    → Função para calcular o fatorial de um número
    :param num: número que terá o seu fatorial calculado
    :param show: se True, mostra a sequência do cálculo
    :return: impressão do resultado
    """

    fator = num
    resultado = 1
    seq = ''

    while fator != 0:

        seq += str(fator) + ' x '
        resultado *= fator
        fator -= 1

    if show:
        return print(f'\nO fatorial de {num}! é: {seq[:-3]} = {resultado}')

    else:
        return print(f'\nO fatorial de {num}! é: {resultado}')


valor = ''

while valor.upper() != 'HELP' or not valor.isnumeric():

    valor = input('Digite um número para calcular o seu fatorial ou Help - para ajuda: ')

    if valor.upper() == 'HELP' or valor.isnumeric():
        break

if valor.upper() == 'HELP':
    help(fatorial)

else:

    valor = int(valor)

    if valor > 1:

        while True:

            resp = str(input('Deseja visualizar a sequência de cálculo? (S - Sim | N - Não)')).strip().upper()[0]

            if resp in 'SN':

                if resp == 'S':

                    mostrar = True
                    break

                else:

                    mostrar = False
                    break

    else:
        mostrar = False

    fatorial(valor, show=mostrar)
