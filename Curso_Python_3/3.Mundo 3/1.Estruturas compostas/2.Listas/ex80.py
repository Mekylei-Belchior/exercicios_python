"""
 Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
 já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

"""

valores = []

for i in range(1, 6):

    valor = int(input(f'Digite o {i}º valor: '))

    if i == 1 or valor > valores[-1]:
        valores.append(valor)

    else:

        for j in range(0, len(valores)):

            if valor <= valores[j]:
                valores.insert(j, valor)
                break

print(f'Valores ordenados: {valores}')





