"""
 Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

 A) Quantas pessoas foram cadastradas.
 B) Uma listagem com as pessoas mais pesadas.
 C) Uma listagem com as pessoas mais leves.

"""

pessoas = []
pessoa = []
leves = []
pesadas = []

soma_peso = 0
i = 1

print('-'*50)
print(f'{" CADASTRO DE PESSOAS ":^50}')
print('-'*50)

print()

while True:

    pessoa.append(str(input(f'Digite o nome da {i}ª pessoa: ')).strip())
    pessoa.append(float(input('Digite o peso (Kg): ')))
    pessoas.append(pessoa[:])
    pessoa.clear()

    i += 1

    while True:
        r = str(input('Deseja continuar? (S/N): ')).strip().upper()[0]

        if r in 'SN':
            break

    if r == 'N':
        break

for p in pessoas:
    soma_peso += p[1]

media = soma_peso / len(pessoas)

for p in pessoas:

    if p[1] >= media:
        pesadas.append(p)
        pesadas.sort()

    else:
        leves.append(p)
        leves.sort()

print()
print(f'Pessoas cadastradas: {pessoas}')
print(f'Quantidade de pessoas cadastradas: {len(pessoas)}')
print(f'Média de peso Kg: {media:.2f}')
print()

if len(pessoas) == 1:
    print(f'Foi encontrado somente um cadastro: {pessoas}')

else:
    print(f'Pessoas mais pesadas: {pesadas}')
    print(f'Pessoas mais leves: {leves}')
