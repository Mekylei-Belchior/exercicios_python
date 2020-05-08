"""
 Crie um programa que leia o ano de nascimento de sete pessoas.
 No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

"""

from datetime import date

datas = []
menor = 0
maior = 0

for i in range(1, 8):
    dt = str(input(f'Informe a {i}º data de nascimento: '))
    datas.append(dt)

for data in datas:

    if date.today().year - int(data.split('/')[2]) < 18:
        menor += 1

    else:
        maior += 1

print(f'Quantidade de pessoas que ATINGIRAM a maioridade: {maior}')
print(f'Quantidade de pessoas que NÃO ATINGIRAM  a maioridade: {menor}')
