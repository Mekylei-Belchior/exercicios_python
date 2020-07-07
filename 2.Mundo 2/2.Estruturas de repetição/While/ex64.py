"""
 Crie um programa que leia vários números inteiros pelo teclado.
 O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
 No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

"""

soma = cont = n = 0

n = int(input('Digite um valor ou (999) para finalizar: '))

while n != 999:

    soma += n
    cont += 1

    n = int(input('Digite um valor ou (999) para finalizar: '))

print(f'\nQuantidade de números digitados: {cont}')
print(f'A soma dos números digitados é: {soma}')

