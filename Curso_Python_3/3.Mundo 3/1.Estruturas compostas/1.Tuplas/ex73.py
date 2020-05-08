"""
 Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
 na ordem de colocação. Depois mostre:

 a) Os 5 primeiros times.
 b) Os últimos 4 colocados.
 c) Times em ordem alfabética.
 d) Em que posição está o time da Chapecoense.

"""

clas = ('Flamengo', 'Palmeiras', 'Santos', 'São Paulo', 'Corinthians', 'Internacional', 'Grêmio', 'Bahia',
        'Athletico-PR', 'Goiás', 'Vasco', 'Atlético', 'Botafogo', 'Fortaleza', 'Ceara-SC', 'Fluminense',
        'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

print(f'\nCinco primeiros colocados: {clas[0:5]}')
print(f'Últimos 4 colocados: {clas[-4:]}')
print(f'Times em ordem alfabética: {sorted(clas)}')
print(f'O Chapecoense está na colocação: {clas.index("Chapecoense") + 1}')
