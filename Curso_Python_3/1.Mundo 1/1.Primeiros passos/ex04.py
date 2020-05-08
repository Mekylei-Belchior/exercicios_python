"""
 Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
 e todas as informações possíveis.

"""

dado = input('Digite algo: ')

print(f'O tipo primitivo do dado é: {type(dado)}')
print(f'Só tem espaços: {dado.isspace()}')
print(f'É um número?: {dado.isnumeric()}')
print(f'É alfabético?: {dado.isalpha()}')
print(f'É alfanumérico: {dado.isalnum()}')
print(f'Está em maiúscula: {dado.isupper()}')
print(f'Está em minúscula?: {dado.islower()}')
print(f'Está capitalizado?: {dado.istitle()}')