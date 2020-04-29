"""
 Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
 No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

"""

valores = []

for i in range(1, 5):
    valores.append(int(input(f'Digite o {i}º valor: ')))

print()
print(f'O menor valor é ({min(valores)}) e está na posição ({valores.index(min(valores)) + 1}).')
print(f'O maior valor é ({max(valores)}) e está na posição ({valores.index(max(valores)) + 1}).')

