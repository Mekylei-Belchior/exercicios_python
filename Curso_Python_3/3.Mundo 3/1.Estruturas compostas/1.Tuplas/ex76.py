"""
 Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
 No final, mostre uma listagem de preços, organizando os dados em forma tabular.

"""

print('-'*80)
print(f'{"Lista de Preços":^80}')
print('-'*80)

produtos = ('Arroz', 10.50, 'Feijão', 4.75, 'Leite Condençado', 1.89, 'Macarrão', 2.00, 'Azeite de Oliva', 21.20,
            'Maizena', 2.35, 'Bolacha', 5.56, 'Tomate', 8.20, 'Cenoura', 3.30, 'Laranja', 10.00, 'Pera', 5.60)

for i in range(0, len(produtos), 2):
    print(f'\033[1;33m{produtos[i]:.<71} R$ {produtos[i + 1]:.2f}\033[m')

print('-'*80)