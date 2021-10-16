"""
Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e
mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

Exemplo:
0 – 1 – 1 – 2 – 3 – 5 – 8
"""

print('¬' * 20)
print(f'{"Sequencia de Fibonacci - Python: ":^50}')
print('¬' * 20)

n = int(input('Quantos números da sequencia você quer ver?: '))
print('><' * 15)

n1 = 0
n2 = 1
c = 3
print(f'{n1}→{n2}→', end='')
while c <= n:
    n3 = n1 + n2
    print(f'{n3}→', end='')
    c += 1
    n1 = n2
    n2 = n3
