"""
 Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
 O programa encerrará quando ele disser que quer mostrar 0 termos.

"""

p = int(input('Informe o primeiro termo de uma PA: '))
r = int(input('Informe a razão da PA: '))

ult_elemento = p + (10 - 1) * r
resultado = str(p) + ' → '
continuar = True
termos = 10

while continuar:

    while p < ult_elemento:

        p += r
        resultado += str(p) + ' → '

    print(resultado, end='Pausa')

    t = int(input('\n\nQuantos termos você quer mostrar a mais? '))

    if t > 0:

        termos += t
        ult_elemento = (p + r) + (t - 1) * r
        resultado = ''

    else:

        continuar = False
        print(f'\n\033[1;31mProgressão finalizada com ({termos}) termos mostrados.\033[m')
