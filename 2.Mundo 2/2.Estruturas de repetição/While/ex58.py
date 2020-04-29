"""
  Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
  Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
  foram necessários para vencer.

"""

from random import randint

sorteado = randint(0, 10)
numero = -1
cont = 1

print(f'{"Jogo da Adivinhação: Tente Adivinhar um número de 0 à 10":*^100}\n\n')


while numero != sorteado:
    numero = int(input('\nQual é o número? '))

    if numero != sorteado:
        cont += 1
        print('Você errou. Tente novamente!')

    else:
        print(f'\033[1;36mParabéns. Você acertou o número com ({cont}) tentativas!\033[m')
