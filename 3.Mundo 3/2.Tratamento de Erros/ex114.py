"""
 Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

"""

import socket

try:
    site = 'pudim.com.br'
    teste = socket.gethostbyname(site)
    site = site.split('.')

except socket.gaierror:
    print(f'\033[1;31mO site não está acessível no momento!\033[m')

else:
    print(f'\033[1;33mO site \"{site[0]}\" do host ({teste}), foi acessado com sucesso!\033[m')
