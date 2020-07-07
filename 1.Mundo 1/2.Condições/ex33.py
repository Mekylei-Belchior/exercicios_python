"""
 Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.

"""

n1 = int(input('Informe o primeio número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))

menor = n1
maior = n1

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O menor número é: {} \nO maior número é: {}'.format(menor, maior))