"""
 Faça um programa que leia o nome completo de uma pessoa.
 Mostre o primeiro e o último nome separadamente.

"""

nome = input('Digite seu nome completo: ').strip()

print(f'Prazer em te conhecer, {nome.title()}.')
print(f'Seu primeiro nome é: {nome.split()[0].title()}')
print(f'Seu último nome é: {nome.split()[-1].title()}')
