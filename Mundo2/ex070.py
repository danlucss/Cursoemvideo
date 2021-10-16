"""
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato
"""

print('LOJA DAS TREVAS')
tot = mmil = c = menor = maior = 0
barato = ''
while True:
    prod = str(input('Informe o nome do produto: '))
    prec = float(input('Informe o preço do produto: '))
    c += 1
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar adcionando produtos? [S/N] ')).strip().upper()
    tot += prec
    if prec >= 1000.00:
        mmil += 1

    if c == 1:
        menor = prec
    else:
        if prec < menor:
            menor = prec
            barato = prod
    if escolha in 'N':
        break
print(f'O total gasto foi de: R${tot:.2f}.')
print(f'Ao todo {mmil} produtos custam mais de R$1000.00.')
print(f'O produto mais barato foi {barato}, que custou RS{menor}.')
