"""
 Crie um programa que leia um nome de uma pessoa e diga se ela tem
 "Soares" no nome.

"""

nome = input('Digite um nome completo: ').strip().lower()

print(f'O nome possui (Soares)?: {"soares" in nome}')
