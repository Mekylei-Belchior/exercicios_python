"""
 Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
 Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
 acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

"""

from datetime import date

empregado = {}

empregado['Nome'] = str(input('Nome: ')).strip()
nascimento = int(input('Ano de nascimento: '))
empregado['Idade'] = date.today().year - nascimento
empregado['CTPS'] = int(input('Carteira de Trabalho (0 - Não possui): '))

if empregado['CTPS'] != 0:

    empregado['Ano Contratação'] = int(input('Ano de contratação: '))
    empregado['Salário'] = float(input('Salário R$: '))
    empregado['Aposentadoria'] = (empregado['Ano Contratação'] + 35) - nascimento

print()
print(f'{"*** INFORMAÇÕES DO TRABALHADOR ***"}\n')

for k, v in empregado.items():
    print(f'- {k} tem o valor {v}')
