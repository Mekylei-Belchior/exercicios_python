"""
 Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
 que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

"""

numeros = [[], []]

for i in range(1, 8):

    n = int(input(f'Digite o {i}º número: '))

    if n % 2 == 0:
        numeros[0].append(n)

    else:
        numeros[1].append(n)

print()
print(f'Números pares: {sorted(numeros[0])}')
print(f'Números ímpares: {sorted(numeros[1])}')
