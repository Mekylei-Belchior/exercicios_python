"""
  Crie um programa que leia o nome completo de uma pessoa e mostre:

  - O nome com todas as letras maiúsculas;
  - O nome com todas as letras minúsculas;
  - Quantas letras no total (sem considerar espaços);
  - Quantas letras tem o primeiro nome.

"""

nome = str(input('Digite um nome completo: '))

print(f'Nome em Maiúsculo: {nome.upper()}')
print(f'Nome em Minúsculo: {nome.lower()}')

nome = nome.split()
tamanho = len(''.join(nome))

print(f'Total de letras (sem espaços): {tamanho}')
print(f'O primeiro nome ({nome[0]}) tem ({len(nome[0])}) letras.')