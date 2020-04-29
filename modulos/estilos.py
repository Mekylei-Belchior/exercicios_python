def cores(cor='sem'):
    """
    → Função para formatação de cores
    :param cor: a ser aplicada
    :return: a cor
    """

    cores = {'sem':      '\033[m',       # 0 - sem cor
             'branco':   '\033[7;30m',   # 1 - branco
             'vermelho': '\033[1;31m',   # 2 - vermelho
             'verde':    '\033[1;32m',   # 3 - verde
             'amarelo':  '\033[1;33m',   # 4 - amarelo
             'azul':     '\033[1;34m',   # 5 - azul
             'roxo':     '\033[1;35m',   # 6 - roxo
             'magenta':  '\033[1;33m',   # 7 - magenta
             'cinza':    '\033[1:37m'    # 8 - cinza
             }

    return cores[cor]

