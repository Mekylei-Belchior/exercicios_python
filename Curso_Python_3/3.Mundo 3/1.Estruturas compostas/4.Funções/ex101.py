""""
 Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
 retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

"""


def voto(ano):

    from datetime import date

    anoAtual = date.today().year
    idade = anoAtual - ano

    if 18 <= idade <= 70:
        return print(f'Com {idade} anos: Voto OBRIGATÓRIO!')

    elif 16 <= idade <= 17 or idade > 70:
        return print(f'Com {idade} anos: Voto OPCIONAL')

    else:
        return print(f'Com {idade} anos: Voto NEGADO!')


ano = int(input('Ano de nascimento: '))
voto(ano)
