"""
 Escreva um programa que pergunte o salário do funcionário e calcule o seu aumento.
 Para salários superiores a (R$ 1.250,00), calcule um aumento de 10%. Para salários
 inferior ou iguais, o almento é de 15%.

"""

sal = float(input('Qual o seu salário? '))

if sal <= 1250.00:
    print(f'O valor do seu salário reajustado é: R$ {(sal * 15 / 100) + sal:.2f}')

else:
    print(f'O valor do seu salário reajustado é: R$ {(sal * 10 / 100) + sal:.2f}')