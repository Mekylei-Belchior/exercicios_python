"""
 Crie um programa que leia um nome de uma cidade e diga se ele começa ou não
 com o nome "Santo".

"""

cidade = input('Digite o nome da cidade: ').strip().lower().split()

print('santo' in cidade)