"""
 Faça um programa que leia um número qualquer e mostre o seu fatorial
    Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

"""

f = fator = int(input('Resolver o fatorial de: '))

resultado = 1
fatorial = ''

while fator != 0:

    fatorial += str(fator) + ' x '
    resultado *= fator
    fator -= 1

print(f'Fatorial de {f}! = {fatorial[:-2]}= {resultado}')

"""

f = fator = int(input('Resolver o fatorial de: '))

resultado = 1
fatorial = ''

for i in range(fator, 0, -1):
    fatorial += str(fator) + ' x '
    resultado *= fator
    fator -= 1

print(f'Fatorial de {f}! = {fatorial[:-2]}= {resultado}')

"""