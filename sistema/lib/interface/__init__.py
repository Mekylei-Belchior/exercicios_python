def cores(cor='sem'):
    """
    → Função para formatação de cores
    :param cor: a ser aplicada
    :return: a cor
    """

    cores = {

             'sem':      '\033[m',       # 0 - sem cor
             'branco':   '\033[1;30m',   # 1 - branco
             'vermelho': '\033[1;31m',   # 2 - vermelho
             'verde':    '\033[1;32m',   # 3 - verde
             'amarelo':  '\033[1;33m',   # 4 - amarelo
             'azul':     '\033[1;34m',   # 5 - azul
             'roxo':     '\033[1;35m',   # 6 - roxo
             'magenta':  '\033[1;36m',   # 7 - magenta
             'cinza':    '\033[1:37m'    # 8 - cinza

    }

    return cores[cor]


def linha(tm=50, simb='-'):
    """
    → Função para criar uma linha
    :param tm: tamanho da linha
    :param simb: símbolo para formação da linha
    :return: a linha
    """
    return print(simb * tm)


def cabecalho(texto, tm=50):
    """
    → Função para inserir um cabeçalho
    :param texto: do cabeçalho
    :param tm: quantidade de caracterestes
    """

    linha()
    print(f'{texto.center(tm)}')
    linha()


def leia_int(texto):
    """
    → Funcção para validar números inteiros.
    :param texto: a ser exibido ao usuário
    :return: um número inteiro
    """

    try:
        valor = int(input(texto))

        if valor < 0:
            raise ValueError

    except (ValueError, TypeError):
        print(f'{cores("vermelho")}Valor inválido. Digite um número inteiro!{cores("sem")}')

        return leia_int(texto)

    except:
        print(f'\n{cores("vermelho")}O usuário preferiu não digitar esse número!{cores("sem")}')

        return 0

    else:
        return valor


def leia_texto(texto):

    try:

        texto = str(input(texto)).strip()

    except:

        print(f'\n{cores("vermelho")}O usuário decidiu finalizar o processo via comando de teclado.{cores("sem")}')
        exit(0)

    else:

        txt = texto.split()
        novo_texto = ''

        for t in txt:
            novo_texto += t

        if not novo_texto.isalpha():

            print(f'{cores("vermelho")}Valor inválido. Digite um nome válido!{cores("sem")}')

            return leia_texto(texto)

        else:

            return texto


def menu(lista):
    """
    → Função para exibir o menu principal.
    :param lista: com os itens que compõem o menu
    :return: a opção escolhida
    """

    cabecalho('MENU PRINCIPAL')

    for p, i in enumerate(lista):

        print(f'{cores("amarelo")}{p + 1} - {cores()}{cores("azul")}{i}{cores()}')

    linha()

    op = leia_int(f'{cores("verde")}Sua opção:{cores()} ')

    return op

