def aumentar(valor=0, percentual=0, formatado=False):
    """
    → Função para aumentar o valor de acordo com o percentual.
    :param valor: que será aumentado
    :param percentual: que será aplicado ao valor
    :param formatado: se True, mostra o valor formatado
    :return: o valor com o reajuste percentual
    """

    resultado = valor + (valor * percentual / 100)

    return resultado if not formatado else moeda(resultado)


def diminuir(valor=0, percentual=0, formatado=False):
    """
    → Função para diminuir o valor de acordo com o percentual.
    :param valor: que será reduzido
    :param percentual: que será aplicado ao valor
    :param formatado: se True, mostra o valor formatado
    :return: o valor com o reajuste percentual
    """

    resultado = valor - (valor * percentual / 100)

    return resultado if not formatado else moeda(resultado)


def dobro(valor=0, formatado=False):
    """
    → Função para dobrar um valor
    :param valor: que será dobrado
    :param formatado: se True, mostra o valor formatado
    :return: valor dobrado
    """

    resultado = valor * 2

    return resultado if not formatado else moeda(resultado)


def metade(valor=0, formatado=False):
    """
    → Função para dividir um valor ao meio
    :param valor: que será divido
    :param formatado: se True, mostra o valor formatado
    :return: do valor dividio ao meio
    """

    resultado = valor / 2

    return resultado if not formatado else moeda(resultado)


def moeda(valor=0.0, moeda='R$'):
    """
    → Função para formatar o valor para o padrão monetário.
    :param valor: a ser formadado
    :param moeda: tipo da moeda
    :return: valor formatado ou não formatado
    """

    return f'{moeda} {valor:.2f}'.replace('.', ',')


def resumo(valor, per_mais, per_menos):
    """
    → Função para mostrar o resumo de um valor
    :param valor: a ser resumido
    :param per_mais: percentual de aumento que será aplicado ao valor
    :param per_menos: percentual de redução que será aplicado ao valor
    """
    tm = 30
    print('-' * tm)
    print(f'{"RESUMO DO VALOR":^{tm}}')
    print('-' * tm)

    print(f'Preço analisado: \t{str(moeda(valor))}')
    print(f'Dobro do preço: \t{str(dobro(valor, True))}')
    print(f'Metade do preço: \t{str(metade(valor, True))}')
    print(f'{per_mais}% de aumento: \t{str(aumentar(valor, per_mais, True))}')
    print(f'{per_menos}% de redução: \t{str(diminuir(valor, per_menos, True))}')

    print('-' * tm)

