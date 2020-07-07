"""
 Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.  No final do programa, mostre:

 - A média de idade do grupo?
 - Qual é o nome do homem mais velho?
 - Quantas mulheres têm menos de 20 anos?

"""

pessoas = []
soma_idade = 0
velho = 0
nome_velho = 'O grupo não possui homens!'
mulheres = 0

for i in range(0, 4):

        nome = str(input(f'Informe o nome da {i + 1}ª pessoa: ')).strip()
        sexo = str(input(f'Informe o sexo (H - Homem e M - Mulher): ')).upper()

        if sexo == 'H':
            idade = int(input(f'Qual a idade do {nome.upper()}: '))

        else:
            idade = int(input(f'Qual a idade da {nome.upper()}: '))

        pessoas.append([nome, idade, sexo])
        soma_idade += pessoas[i][1]

for pessoa in pessoas:

    if pessoa[2] == 'H' and pessoa[1] > velho:

        nome_velho = pessoa[0]
        velho = pessoa[1]

    if pessoa[2] == 'M' and pessoa[1] < 20:

        mulheres += 1

print('\n', pessoas) # Mostra a relação de pessoas do grupo

print(f'\n\nA idade média do grupo é: {soma_idade / len(pessoas):.0f} anos')
print(f'O nome do homen mais velho é: {nome_velho}')
print(f'A quantidade de mulheres que têm nemos de 20 anos é: {mulheres} ')
