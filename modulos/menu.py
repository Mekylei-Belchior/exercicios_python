from módulos import estilos as e
from módulos import resumo as r, cadastrar as c, sair as s
from utilidades import dado as d


def menu():

    print('-' * 30)
    print(f'{"MENU PRINCIPAL":^30}')
    print('-' * 30)
    print(f'{e.cores("amarelo")}1 - {e.cores()}{e.cores("azul")}Ver pessoas cadastradas{e.cores()}\n'
          f'{e.cores("amarelo")}2 - {e.cores()}{e.cores("azul")}Cadastrar nova pessoa{e.cores()}\n'
          f'{e.cores("amarelo")}3 - {e.cores()}{e.cores("azul")}Sair do sistema{e.cores()}')

    print('-' * 30)

    while True:

        op = d.leia_int('Sua opção: ')

        if op == 1:
            r.resumo()
            break

        elif op == 2:
            c.cadastrar()
            break

        elif op == 3:
            s.sair()
            break
