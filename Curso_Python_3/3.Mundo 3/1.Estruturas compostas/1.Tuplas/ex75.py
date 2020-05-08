"""
 Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

 A) Quantas vezes apareceu o valor 9.
 B) Em que posição foi digitado o primeiro valor 3.
 C) Quais foram os números pares.

"""
"""
tupla = (int(input('Digite o 1º valor: ')), int(input('Digite o 2º valor: ')),
         int(input('Digite o 3º valor: ')), int(input('Digite o 4º valor: ')))

"""
tupla = tuple(int(input(f'Digite o {i}º número: ')) for i in range(1, 5))

print(f'\nO número (9) apareceu ({tupla.count(9)}) vezes')

if 3 in tupla:
    print(f'A primeira ocorrência do número (3) foi na posição: {tupla.index(3) + 1}')
else:
    print('O número (3) não aparece na relação')

print('Números pares: ', end='')

for n in tupla:
    if n % 2 == 0:
        print(f'{n} ', end='')
