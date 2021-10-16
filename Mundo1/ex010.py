'''Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
mostre quantos dólares ela pode comprar.'''


dolar = 5.53
din = float(input('Informe quantos R$ quer converter para $: '))
print(f'Você quer converter R${din} para $. ')
print(f'Com R${din:.2f}, você terá ${din/dolar:.2f}.')
