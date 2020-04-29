"""
 Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
 e todos os dicionários em uma lista. No final, mostre:

 A) Quantas pessoas foram cadastradas;
 B) A média de idade;
 C) Uma lista com as mulheres;
 D) Uma lista de pessoas com idade acima da média.

"""

pessoa = {}
grupo = []
mulheres = []
a_media = []
soma_idade = 0

while True:

    nome = str(input('Nome:'))

    while True:

        sexo = str(input('Sexo (H - Homem e M - Mulher): ')).strip().upper()[0]

        if sexo in 'HM':
            break

        print(f'\033[1;31mAtenção...\033[mDigite um valor válido! \033[1;36m(H - Homen | M - Mulher)\033[m\n')

    while True:

        idade = input('Idade: ')

        if idade.isnumeric():
                break

        print(f'\033[1;31mAtenção...\033[m\033[1;36mInforme um número maior ou igual à 0\033[m!')

    pessoa['Nome'] = nome
    pessoa['Sexo'] = sexo
    pessoa['Idade'] = int(idade)
    grupo.append(pessoa.copy())

    while True:

        resp = str(input('\nDeseja continuar (S/N): ')).strip().upper()[0]

        if resp in 'SN':
            break

        print(f'\033[1;31mAtenção...\033[mDigite um valor válido! \033[1;36m(S - Sim | N - Não)\033[m\n')

    if resp == 'N':
        break

for individuo in grupo:

    for k, v in individuo.items():

        if k == 'Idade':
            soma_idade += v

media = soma_idade / len(grupo)

for individuo in grupo:

    for k, v in individuo.items():

        if k == 'Sexo' and v == 'M':
            mulheres.append(individuo.get('Nome'))

for individuo in grupo:

    for k, v in individuo.items():

        if k == 'Idade' and v > media:
            a_media.append(individuo.copy())


print('\n')
print(f'{"========== INFORMAÇÕES DO GRUPO ==========":^50}\n')

print(f'A) Quantidade de pessoas cadastradas: {len(grupo)}')
print(f'B) Média de idade do grupo: {media:.2f}')

if len(mulheres) == 0:
    print('C) O grupo não possui mulheres!')

else:
    print(f'C) Mulheres do grupo: {mulheres}')

if len(a_media) == 0:
    print('D) O grupo não possui pessoas acima da média de idade!')

else:

    print('D) Lista de pessoa(s) que estão com a idade acima da média:\n')

    for individuo in a_media:

        for k, v in individuo.items():
            print(f'    {k:<} = {v:<15}', end='')

        print()
