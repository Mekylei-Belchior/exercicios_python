"""
  Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

"""

pesos = []

for i in range(1, 6):
    p = float(input(f'Informe o peso em Kg, da ({i}º) pessoa: '))
    pesos.append(p)

for i in range(0, len(pesos)):

    for j in range(i + 1, len(pesos)):

        if pesos[j] < pesos[i]:

            aux = pesos[j]
            pesos[j] = pesos[i]
            pesos[i] = aux

print(pesos)
print(f'O maior peso é: {pesos[-1]}Kg')
print(f'O menor peso é: {pesos[0]}Kg')
