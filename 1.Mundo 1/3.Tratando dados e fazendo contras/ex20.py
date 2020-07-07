"""
 O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
 Faça um trabalho que leia o nome dos quatros alunos e mostre a ordem sorteada.

"""

from random import shuffle

a1 = str(input('Informe o nome do primeiro aluno: '))
a2 = str(input('Informe o nome do segundo aluno: '))
a3 = str(input('Informe o nome do terceiro aluno: '))
a4 = str(input('Informe o nome do quarto aluno: '))

alunos = [a1, a2, a3, a4]

shuffle(alunos)
print(f'A ordem de apresentação será: {alunos}')
