"""
 Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

"""

print(f'{"VERIFICADOR DE PALINDROMO":*^40}\n\n')

frase = str(input('Digite uma frase para verificar: ')).strip()
nfrase = str(''.join(frase.split())).lower()

invertido = []

for i in range(len(nfrase) - 1, -1, -1):
    invertido.append(nfrase[i])

invertido = ''.join(invertido)

# print(nfrase)
# print(invertido)

if nfrase == invertido:
    print(f'A frase ({frase}) É UM PALINDROMO.')

else:
    print(f'A frase ({frase}) NÃO É UM PALINDROMO.')
