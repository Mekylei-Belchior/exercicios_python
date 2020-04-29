"""
 Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
 Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
 A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

"""

print('*-*' * 30)
print(" " + '\033[1;36mSIMULADOR DE EMPRÉSTIMO\033[m'.center(80) + " ")
print('*-*' * 30)

valor = float(input('Qual é o valor da casa? '))
sal = float(input('Qual é o seu salário? '))
ano = int(input('Você irá dividir o valor em quantos anos? '))

max_parcela = sal * (30 / 100)
parcelas = ano * 12
v_parcela = valor / parcelas

if v_parcela > max_parcela:

    print('\nEmpréstimo \033[1;31mNÃO AUTORIZADO\033[m!. O valor da parcela excedeu o valor permitido.')
    print(f'\nValor da casa: R$ {valor:.2f}\n'
          f'Salário: R$ {sal:.2f}\n'
          f'Parcelas: {parcelas}\n'
          f'Valor das parcelas: R$ {v_parcela:.2f}')
else:

    print('\nEmpréstimo \033[1;35mAUTORIZADO\033[m!')
    print(f'\nValor da casa: R$ {valor:.2f}\n'
          f'Salário: R$ {sal:.2f}\n'
          f'Parcelas: {parcelas}\n'
          f'Valor das parcelas: R$ {v_parcela:.2f}')
