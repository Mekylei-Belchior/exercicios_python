"""
  Crie um programa que leia vários números inteiros pelo teclado.
  No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
  O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

"""

md = 0
valores = []

continuar = True

while continuar:

    n = int(input('Digite um número: '))
    valores.append(n)

    check = str(input('\nDeseja continuar. Sim ou Não? ')).strip().upper()[0]

    while check not in 'SN':

        print('\n\033[1;31mOpção inválida. Tente novamente!\033[m')
        check = str(input('\n\nDeseja continuar. Sim ou Não? ')).strip().upper()[0]

    if check == 'N':
        continuar = False

md = sum(valores) / len(valores)
valores.sort()

print(f'\n\nA média dos valores digitados é: {md}')
print(f'O menor valor é ({valores[0]}) e o maior valor é ({valores[-1]})')







