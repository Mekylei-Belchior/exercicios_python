"""
 Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
 com as seguintes informações:

 - Quantidade de notas;
 - A maior nota;
 - A menor nota;
 - A média da turma;
 - A situação (opcional).

 Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

"""


def nota(* notas, situacao=False):
    """
    → Programa para avaliar a sitiação dos alunos
    :param notas: notas dos alunos
    :param situacao: se True, mostra a situação dos alunos
    :return: um dicionário com as informações
    """

    dados = dict()

    dados['Total'] = len(notas)
    dados['Maior'] = max(notas)
    dados['Menor'] = min(notas)
    dados['Média'] = sum(notas) / len(notas)

    if situacao:

        if dados['Média'] >= 7:
            dados['Situação'] = 'BOM'

        elif 5 <= dados['Média'] < 7:
            dados['Situação'] = 'RAZOÁVEL'

        else:
            dados['Situação'] = 'RUIM'

    return dados


resp = nota(5.7, 2.9, 0.8, 6.5, situacao=True)
print(resp)
