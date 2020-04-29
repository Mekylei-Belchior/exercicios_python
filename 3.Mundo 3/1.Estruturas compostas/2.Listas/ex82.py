"""
 Crie um programa que vai ler vários números e colocar em uma lista.
 Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
 respectivamente. Ao final, mostre o conteúdo das três listas geradas.

"""

valores = []
impar = []
par = []

while True:

    valores.append(int(input('Digite um valor: ')))

    while True:
        resp = str(input('Deseja continuar? (S/N): ')).strip().upper()[0]

        if resp in 'SN':
            break

    if resp == 'N':
        break

for valor in valores:

    if valor % 2 == 0:
        par.append(valor)

    else:
        impar.append(valor)

print()
print(f'Valores digitados: {valores}')
print(f'Valores pares: {par}')
print(f'Valores ímpares: {impar}')
