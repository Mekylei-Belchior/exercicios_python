"""
 Desenvolva um programa que pergunte a distância de uma viagem em km.
 Calcule o preço da passagem , cobrando R$ 0,50 por km para viagens até 200km e 0,45 para viagens mais longas.

"""

km = int(input('Qual a distância da viagem? '))

if km > 200:
    valor = float(km * 0.45)
    print(f'O preço da viagem será: R$ {valor:.2f} ')

else:
    valor = float(km * 0.50)
    print(f'O preço da viagem será: R$ {valor:.2f}')
