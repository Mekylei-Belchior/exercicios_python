def leia_dinheiro(texto):
    """
    → Função para leitura e validação de um valor monetário.
    :param texto: a ser apresentado para o usuário
    :return: um valor do tipo float
    """

    while True:

        valor = str(input(texto)).strip().replace(',', '.')

        if valor.replace('.', '').isnumeric():
            break

        print(f'\033[1;31mO valor digitado \"{valor}\", é um preço inválido!\033[m')

    return float(valor)


def leia_int(texto):
    """
    → Funcção para validar números inteiros.
    :param texto: a ser exibido ao usuário
    :return: um número inteiro
    """

    try:
        valor = int(input(texto))

    except (ValueError, TypeError):
        print(f'\033[1;31mValor inválido. Digite um número inteiro!\033[m')

        return leia_int(texto)

    except:
        print(f'\n\033[1;31mO usuário preferiu não digitar esse número!\033[m')

        return 0

    else:
        return valor


def leia_float(texto):
    """
    → Funcção para validar números de ponto flutuante (número real).
    :param texto: a ser exibido ao usuário
    :return: um número de ponto flutuante
    """

    try:
        valor = float(input(texto))

    except (ValueError, TypeError):
        print(f'\033[1;31mValor inválido. Digite um número real!\033[m')

        return leia_float(texto)

    except:
        print(f'\n\033[1;31mO usuário preferiu não digitar esse número!\033[m')

        return 0

    else:

        return valor

