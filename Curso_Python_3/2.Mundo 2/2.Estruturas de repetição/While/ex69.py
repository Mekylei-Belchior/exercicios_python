"""
 Crie um programa que leia a idade e o sexo de várias pessoas.
 A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

 A) quantas pessoas tem mais de 18 anos.
 B) quantos homens foram cadastrados.
 C) quantas mulheres tem menos de 20 anos

"""
maior = homem = mulher = 0

while True:

    print('-'*50)

    idade = int(input('\nIdade: '))

    sexo = 'a'

    while sexo not in 'HM':
        sexo = str(input('Sexo (H - Homem e M - Mulher): ')).strip().upper()[0]

    print('-'*50, '\n')

    if idade > 18:
        maior += 1

    if sexo == 'H':
        homem += 1

    if sexo == 'M' and idade < 20:
        mulher += 1

    resp = 'a'

    while resp not in 'SN':
        resp = str(input('\nDeseja continuar (S - Sim e N - Não): ')).strip().upper()[0]

    if resp == 'N':
        break

print(f'\n\nQuantidade de pessoas maiores de 18 anos: {maior}')
print(f'Quantidade de homens cadastrados: {homem}')
print(f'Quantidade de mulheres com menos de 20 anos: {mulher}')