"""
  Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

 - EQUILÁTERO: todos os lados iguais;
 - ISÓSCELES: dois lados iguais, um diferente;
 - ESCALENO: todos os lados diferentes.

"""

r1 = float(input('Informe o valor da primeira reta do triângulo: '))
r2 = float(input('Informe o valor da segunda reta do triângulo: '))
r3 = float(input('Informe o valor da terceira reta do triângulo: '))

if abs(r2 - r3) < r1 < (r2 + r3):
    print(f'\nOs valores ({r1}, {r2}, {r3}), das retas informadas, PODEM formar um triângulo!')

    if r1 == r2 == r3:
        print('As retras formam um triângulo: EQUILÁTERO')

    elif r1 != r2 != r3 != r1:
        print('As retas formam um triângulo: ESCALENO.')

    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print('As retas formam um triângulo: ISÓCELES.')

else:
    print(f'\nOs valores ({r1}, {r2}, {r3}), das retas informadas, NÂO PODEM formar um triângulo!')
