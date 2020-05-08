"""
 Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
 No final, mostre o conteúdo da estrutura na tela.

"""

aluno = dict()

aluno['Nome'] = str(input('Nome: ')).strip()
aluno['Média'] = float(input('Média: '))

if aluno['Média'] >= 7.0:
    aluno['Situação'] = 'Aprovado'

elif 5.0 <= aluno['Média'] < 7.0:
    aluno['Situação'] = 'Recuperação'

else:
    aluno['Situação'] = 'Reprovado'

print()
print('-'*30, '\n')

for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
