"""
 Faça um programa que calcule a soma entre todos os números que são múltiplos de três
 e que se encontram no intervalo de 1 até 500.

"""

soma = 0
qtde = 0
numero = []

for i in range(1, 501, 2):

    if i % 3 == 0:
        qtde += 1
        numero.append(i)

for n in numero:
    soma += n

print(f'A soma dos {qtde} números ímpares e multiplos de 3, de 1 até 500 é: {soma}')
print(numero, end=' ')