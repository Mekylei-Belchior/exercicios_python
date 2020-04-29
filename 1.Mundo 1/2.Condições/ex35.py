"""
 Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
 se elas podem ou não formar um triângulo.

 Obs.: Para construir um triângulo é necessário que a medida de qualquer um dos lados
       seja menor que a soma das medidas dos outros dois e maior que o valor absoluto
       da diferença entre essas medidas.

"""

r1 = int(input('Informe o comprimento da primeira reta: '))
r2 = int(input('Informe o comprimento da segunda reta: '))
r3 = int(input('Informe o comprimento da terceira retra: '))

cores = {'verde': '\033[1;33m', 'vermelho': '\033[1;31m', 'limpa': '\033[m'}

print(f'{cores["verde"]}PODE formar um triângulo!{cores["limpa"]}' if abs((r2 - r3)) < r1 < (r2 + r3) else
      f'{cores["vermelho"]}NÃO pode formar um triângulo!{cores["limpa"]}')
