"""
 Faça um programa que leia um número de 0 à 9999 e mostre na tela cada um dos digítos separados.

 Ex.: 1834

 Unidade: 4
 Dezena: 3
 Centena: 8
 Milhar: 1

"""


num = int(input('Digite um número de 0 à 9999: '))

print(f'Número informado: {num} '
      f'\n\nUnidade: {num // 1 % 10} '
      f'\nDezena: {num // 10 % 10} '
      f'\nCentena: {num // 100 % 10} '
      f'\nMilhar: {num // 1000 % 10}')
