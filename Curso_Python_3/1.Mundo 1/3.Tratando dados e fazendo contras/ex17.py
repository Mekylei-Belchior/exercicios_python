"""

 Faça um programa que leia o comprimento do cateto oposto e do cateto
 adjacente de um triângulo retângulo, calcule e mostre o comprimento
 da hipotenusa.

"""
from math import hypot

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

hipotenusa =  (co**2 + ca**2)**(1/2)

print(f'O comprimento da hipotenusa é: {hypot(co,ca)}')
print(f'Hipotenusa: {hipotenusa}')