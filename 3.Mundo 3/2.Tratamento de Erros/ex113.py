"""
 Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número
 de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

"""

from utilidades import dado


i = dado.leia_int('Digite um número inteiro: ')
r = dado.leia_float('Digite um número real: ')

print(f'O número inteiro digitado foi {i} e o real foi {r}')
