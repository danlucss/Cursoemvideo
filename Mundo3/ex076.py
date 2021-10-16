"""
Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

tupla_mercado = ("Sabão em pó", 16.99,
                 "Detergente", 1.29,
                 "Arroz cristal", 22.99,
                 "Alcatra", 38.90,
                 "Chocolate", 12.99)
print('-' * 30)
print('LISTA DE PREÇOS')
print('-' * 30)
for pos in range(0, len(tupla_mercado)):
    if pos % 2 == 0:
        print(f'{tupla_mercado[pos]:.<30}', end='')
    else:
        print(f'R${tupla_mercado[pos]:>5}')
