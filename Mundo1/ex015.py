'''
Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
 e a quantidade de dias pelos quais ele foi alugado.
 Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''

c = input('Qual carro você alugou? ')
km = float(input('Quantos km você andou com o carro? '))
d = int(input('Por quantos dias você o alugou? '))
kmt = km * 0.15
dt = d * 60
print(f'O carro que você alugou é um {c}, por dia você pagará {dt}R$, e por KM {kmt}R$. Totalizando: {dt + kmt}R$.')
