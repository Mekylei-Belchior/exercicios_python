"""
 Crie um programa que leia o nome completo de uma pessoa e mostre:
 - O nome com todas as letras em maiúscula e minúscula;
 - Quantas letras ao todo sem considerar espaços;
 - Quantas letras tem o primeiro nome.

"""

nome = input('Digite seu nome completo: ').strip()
print(f'Nome em maiúsculo: {nome.upper()}')
print(f'Nome em minúsculo: {nome.lower()}')
print(f'Quantidade de letras: {len(nome) - nome.count(" ")}')
print(f'Quantidade de letras do primeiro nome: {len(nome.split()[0])}')