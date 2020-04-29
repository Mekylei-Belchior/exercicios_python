"""
 Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
 o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
 mesmo que algum dado não tenha sido informado corretamente.

"""


def ficha(nomes='<desconhecido>', gols=0):
    """
    → função para mostrar a ficha de jogadores
    :param nomes: nome do jogador
    :param gols: quantidade de gols feito pelo jogador
    :return: impressão com os valores recebidos como parâmetro
    """

    return print(f'\nO jogador {nomes} fez {gols} gol(s) no campeonato.')


nome = str(input('Nome do jogador: ')).strip()
gol = str(input('Número de gols: ')).strip()

if nome != '' and not gol.isnumeric():
    ficha(nome)

elif gol.isnumeric() and nome == '':
    ficha(gols=int(gol))

elif nome == '' and not gol.isnumeric():
    ficha()

else:
    ficha(nome, int(gol))
