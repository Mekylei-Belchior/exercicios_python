"""
 Crie um programa que leia o nome e o preço de vários produtos.
 O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

 A) qual é o total gasto na compra.
 B) quantos produtos custam mais de R$1000.
 C) qual é o nome do produto mais barato.

"""
total = mais = menor = 0
cont = 1
barato = ''

while True:

    nome = str(input('\nNome do produto: ')).strip()
    valor = float(input('Preço: '))

    total += valor

    if valor > 1000:
        mais += 1

    if cont == 1 or valor < menor:
        menor = valor
        barato = nome

    cont += 1
    resp = 'a'

    while resp not in 'SN':
        resp = str(input('\nDeseja continuar cadastrando (S - Sim e N - Não)? ')).strip().upper()[0]

    if resp == 'N':
        break

print(f'\n\nTotal gasto na compra: R$ {total:.2f}')
print(f'Quantos produtos custam mais de R$1000: {mais}')
print(f'O nome do produto mais barato é: {barato}  Valor: R$ {menor:.2f}')
