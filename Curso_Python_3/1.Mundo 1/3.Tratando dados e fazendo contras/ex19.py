"""
 Um professor quer sortear um dos seus quatros alunos para apagar o quadro.
 Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

"""

from random import choice

alunos = []

a1 = str(input('Informe o nome do primeiro aluno: '))
alunos.append(a1)

a2 = str(input('Informe o nome do segundo aluno: '))
alunos.append(a2)

a3 = str(input('Informe o nome do terceiro aluno: '))
alunos.append(a3)

a4 = str(input('Informe o nome do quarto aluno: '))
alunos.append(a4)

escolhido = choice(alunos)
print(f'O aluno escolhido foi: {escolhido}')

