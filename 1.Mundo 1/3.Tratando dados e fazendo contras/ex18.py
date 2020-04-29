"""
 Faça um programa que leia um ângulo e mostre na tela o valor do seno,
 cosseno e tangente deste ângulo.

"""

from math import sin, cos,tan

angulo = int(input('Informe o valor do ângulo: '))

print(f'Seno {angulo}: {sin(angulo)} \nCosseno {angulo}: {cos(angulo)} \nTangente {angulo}: {tan(angulo)}')