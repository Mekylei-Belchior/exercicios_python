"""
 Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
 No final, mostre os 10 primeiros termos dessa progressão.

"""

p = int(input('Informe o primeiro termo de uma PA: '))
r = int(input('Informe a razão da PA: '))
decimo = p + (10 - 1) * r

for n in range(p, decimo + r, r):

    print(n, end=' -> ')

print('Fim.')
