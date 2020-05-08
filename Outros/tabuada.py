# -*- coding: UTF-8 -*-

"""
 Crie um programa que leia um operador aritmético e imprima a sua tabuada.

"""


def tabuada(op):
    """
    Calcula a tabuada de divisão, multiplicação, soma e subtração.

    Arguments:
        op: str -> Operador

    Return:
        Uma lista com a tabuada. 
    """

    if op == '*':
        return [f'{i} x {j} = {i * j}' for i in range(1, 11) for j in range(1, 11)]
    elif op == '/':
        return [f'{j} ÷ {i} = {int(j / i)}' for i in range(1, 11) for j in range(i, (i * 10) + 1, i)]
    elif op == '+':
        return [f'{i} {op} {j} = {i + j}' for i in range(1, 11) for j in range(1, 11)]
    elif op == '-':
        return [f'{j} {op} {i} = {j - i}' for i in range(1, 11) for j in range(i + 1, 11 + i)]


while True:
    operador = str(input('\nInforme um dos operadores ([ / ], [ * ], [ + ], [ - ]): '))

    if not operador is '' and operador in '/*+-':

        resultados = tabuada(operador)
        print()

        [print(f'{resultado:^14}') for resultado in resultados]
        break
