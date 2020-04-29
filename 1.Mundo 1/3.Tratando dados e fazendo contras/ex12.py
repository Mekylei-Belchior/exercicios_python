"""

 Faça um programa que leia a largura de uma parede em metros,
 calcule sua área e a quantidade de tinta necessária para pintá-la.
 Sabendo que cada litro de tinta, printa uma área de 2m².

"""


largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))
area = largura * altura

print(f'A área da parede é: {area}')
print(f'A quantidade de tinta para pintar a parede é: {area/2} lt')