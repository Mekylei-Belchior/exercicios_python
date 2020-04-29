"""
 Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
 (largura e comprimento) e mostre a área do terreno.

"""

def area(l, c):

    print(f'A área de um terreno ({l} x {c}) é de {l * c:.1f}m².')


titulo = 'Controle de Terrenos'
print(titulo)
print('-' * len(titulo), '\n')

l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))

area(l, c)
