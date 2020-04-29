"""

 Crie um programa que leia quanto dinheiro uma pessoa tem na carteria e mostre
 quantos doláres ela pode comprar.

 US$ 1,00 = R$ 3,27
"""


valor = float(input('Quanto reais você possui? '))

print(f'A quantia que você possui (R$ {valor:.2f} Reais) é equivalente a: US$ {valor/3.27:.2f} Doláres ')
