"""
 Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
 só que agora utilizando um laço for.

"""

n = int(input('Deseja visualizar a tabuada de qual número? '))

for i in range(1, 11):
    print(f'{n} x {i} = {n * i}')
