from sistema.lib.interface import *
from sistema.lib.processo import *
from time import sleep


while True:

    r = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])

    if r == 1:

        cabecalho('PESSOAS CADASTRADAS')
        listar()

    elif r == 2:

        cabecalho('NOVO CADASTRO')
        dados = dados_pessoa()
        cadastrar(dados[0], dados[1])

    elif r == 3:
        cabecalho(f'{cores("branco")}Programa finalizado. Até logo!{cores()}')
        break

    else:
        print(f'{cores("vermelho")}Opção inválida. Tente novamente!{cores()}')

    sleep(1)
