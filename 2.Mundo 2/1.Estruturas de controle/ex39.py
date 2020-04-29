"""
 Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
 se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
 do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

"""
from datetime import date

ano = int(input('Informe o seu ano de nascimento: '))

idade = date.today().year - ano

if idade < 18:
    print(f'Você deverá se alistar em {18 - idade} ano(s).')

elif idade == 18:
    print('Você possui 18 anos. Aliste-se já!')

else:
    print(f'Você deveria ter se alistado em {idade - 18} ano(s) atrás.')
