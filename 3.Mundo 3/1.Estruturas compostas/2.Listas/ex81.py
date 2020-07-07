"""
 Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:

 A) Quantos números foram digitados.
 B) A lista de valores, ordenada de forma decrescente.
 C) Se o valor 5 foi digitado e está ou não na lista.

"""

valores = []

while True:

    valor = int(input('Digite um valor: '))
    valores.append(valor)

    while True:
        resp = str(input('Deseja inserir outro valor? S - Sim e N - Não: ')).strip().upper()[0]

        if resp in 'SN':
            break

    if resp == 'N':
        break

print()
print(f'Foram digitados ({len(valores)}) valor(es).')

valores.sort(reverse=True)
print(f'Os valores ordenados de forma decrescente: {valores}')

if 5 in valores:
    print(f'O valor (5) foi digitado ({valores.count(5)})vez(es).')

else:
    print('O valor (5) NÃO FOI digitado.')
