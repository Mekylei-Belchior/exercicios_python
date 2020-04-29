"""
 Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
 qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

"""

num = int(input('Informe um número para conversão: \n'))

converter = int(input('Converter para: '
                      '\n\033[1;31m[1] - Binário\033[m '
                      '\n\033[1;33m[2] - Octal\033[m '
                      '\n\033[1;34m[3] - Hexadecimal\033[m '))

if converter == 1:
    print(f'O número ({num} convertido para Binário é: {bin(num)[2:]})')

elif converter == 2:
    print(f'O número ({num}) convertido para Octal é: {oct(num)[2:]}')

elif converter == 3:
    print(f'O número ({num}) convertido para Hexadecimal é: {hex(num)[2:]}')

else:
    print('\nOpção inválida!')
