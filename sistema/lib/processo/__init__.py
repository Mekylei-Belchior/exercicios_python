from sistema.lib.interface import cores, leia_int, leia_texto


def dados_pessoa():
    """
    →Função para obter os dados da pessoa
    :return: o nome e idade da pessoa
    """
    nome = leia_texto('Nome: ')
    idade = leia_int('Idade: ')

    return nome, idade


def cadastrar(nome, idade):
    """
    → Função para cadastrar pessoas.
    :param nome: da pessoa
    :param idade: da pessoa
    """

    import os.path as file

    try:

        if file.exists('Cadastros.txt'):

            arquivo = open('Cadastros.txt', 'a')
            arquivo.writelines([nome, ';', str(idade)])
            arquivo.write('\n')

        else:

            arquivo = open('Cadastros.txt', 'w')
            arquivo.writelines([nome, ';', str(idade)])
            arquivo.write('\n')

        arquivo.close()

    except:
        print(f'{cores("vermelho")}Erro ao manipular o arquivo de dados. Tente novamente!{cores("sem")}')

    else:
        print(f'Novo registro de {cores("branco")}{nome}{cores("sem")} adicionado.')


def listar():
    """
    → Função para listar os cadastros existentes no arquivo de dados.
    """

    try:

        arquivo = open('Cadastros.txt', 'r')
        linhas = arquivo.readlines()

        for linha in linhas:

            pessoa = linha[:-1].split(';')

            print(f'{pessoa[0]:<41}{pessoa[1]:2} ano(s)')

        arquivo.close()

    except:
        print(f'{cores("vermelho")}Erro ao manipular o arquivo de dados. Tente novamente!{cores("sem")}')

