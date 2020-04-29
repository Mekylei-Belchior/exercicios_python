"""
 Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
 Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores
 únicos digitados, em ordem crescente.

"""

valores = []

while True:

    v = int(input('\nCadastre um valor: '))

    if v not in valores:
        valores.append(v)

    else:
        print(f'\n\033[1;31mCadastro NÃO REALIZADO! O valor ({v}) Já está cadastro.\033[m')

    while True:
        resp = str(input('\nDeseja cadastrar novo valor (S - Sim e N - Não)? ')).strip().upper()[0]

        if resp in 'SN':
            break

    if resp == 'N':
        break

valores.sort()
print(f'\nValores cadastrados: {valores}')
