"""
 Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
 e condição de pagamento:

 - à vista dinheiro/cheque: 10% de desconto
 - à vista no cartão: 5% de desconto
 - em até 2x no cartão: preço formal
 - 3x ou mais no cartão: 20% de juros

"""

print(f'{" LOJAS BELCHIOR ":=^40}')

valor = float(input('\nInforme o valor do produto: '))

pgto = int(input('\nESCOLHA A FORMA DE PAGAMENTO:\n'
                 '\n[1] à vista dinheiro/cheque - (10% de desconto)'
                 '\n[2] à vista no cartão - (5% de desconto)'
                 '\n[3] até 2x no cartão - (preço normal)'
                 '\n[4] 3x ou mais no cartão - (20% de juros) '))

if pgto == 1:
    print(f'\n\033[1;31mTotal à pagar (10% de desconto): R$ {valor - (valor * (10 / 100)):.2f}\033[m')
    print(f'Valor do produto: R$ {valor:.2f}')
    print(f'Valor do desconto: R$ {valor * (10 / 100):.2f}')

elif pgto == 2:
    print(f'\n\033[1;31mTotal à pagar (5% de desconto): R$ {valor - (valor * (5 / 100)):.2f}\033[m')
    print(f'Valor do produto: R$ {valor:.2f}')
    print(f'Valor do desconto: R$ {valor * (5 / 100):.2f}')

elif pgto == 3:
    parcela = int(input('Dividir em 1 ou 2 parcelas? '))

    if 1 <= parcela <= 2:

        print(f'\n\033[1;31mTotal à pagar (sem desconto): R$ {valor:.2f}\033[m')
        print(f'O valor do seu produto foi dividido em {parcela}x parcela(s) de: R$ {valor / parcela:.2f}')
        print(f'Valor do produto: R$ {valor:.2f}')
        print(f'Valor do desconto: R$ {0:.2f}')

    else:

        print('Opção INVÁLIDA. Tente novamente!')

elif pgto == 4:
    parcela = int(input('Dividir em quantas parcelas? '))

    if parcela >= 3:
        total = valor + (valor * (20 / 100))

        print(f'\n\033[1;31mTotal à pagar (20% de juros): R$ {total:.2f}\033[m')
        print(f'O valor do seu produto foi dividido em {parcela}x parcelas de: R$ {total / parcela:.2f}')
        print(f'Valor do produto: R$ {valor:.2f}')
        print(f'Valor do juros: R$ {valor * (20 / 100):.2f}')

    else:

        print('Quantidade de parcelas INVÁLIDA. Tente novamente!')

else:
    print('\nForma de pagamento INVÁLIDA. Tente novamente!')
