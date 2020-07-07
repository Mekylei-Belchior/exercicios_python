"""
 Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
 mostrando os 10 primeiros termos da progressão usando a estrutura while.

"""

p = int(input('Informe o primeiro termo de uma PA: '))
r = int(input('Informe a razão da PA: '))

resultado = str(p)
decimo = p + (10 - 1) * r

while p < decimo:
    p += r
    resultado += ' → ' + str(p)

print(resultado, end=' → Fim.')
