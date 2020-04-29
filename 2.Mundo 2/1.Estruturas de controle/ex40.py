"""
 Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
 de acordo com a média atingida:

 - Média abaixo de 5.0: REPROVADO
 - Média entre 5.0 e 6.9: RECUPERAÇÃO
 - Média 7.0 ou superior: APROVADO

"""

n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Infomre a segunda nota: '))

media = (n1 + n2) / 2

if 50 < media < 70:
    print(f'Sua média é: ({media:.2f}). Você está de RECUPERAÇÃO.')

elif media >= 70:
    print(f'Sua média é: ({media:.2f}). Você está APROVADO!')

else:
    print(f'Sua média é: ({media:.2f}). Você está REPROVADO!')
