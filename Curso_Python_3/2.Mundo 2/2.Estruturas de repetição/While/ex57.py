"""
 Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
 Caso esteja errado, peça a digitação novamente até ter um valor correto.

"""
sexo = ''

while sexo != 'F' and sexo != 'M':

    sexo = str(input('\nInfome o sexo da pessoa (M - Masculino e F - Feminino): ')).upper().strip()

    if sexo == 'F':
        print('A pessoa é do sexo FEMININO!')

    elif sexo == 'M':
        print('O sexo da pessoa é MASCULINO!')

    else:
        print('Valor incorreto. Tente novamente!')
