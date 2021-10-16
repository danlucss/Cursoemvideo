"""
Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""


tot = 0
print('-=-'*10)
print('Calculadora de números primos')
print('Saiba se um número é primo ou não!')
print('-=-'*10)
n = int(input('Informe o número que quer saber: '))
print(f'O número informado é {n}.')
print('Calculando...')
for c in range(1, n + 1):
    print(f'{c}', end=' ')
    if n % c == 0:
        print('\033[32m', end=' ')
        tot += 1
    else:
        print('\033[35m', end=' ')

print(f'\n\033[mO número {n} foi divisivel {tot} vezes.')
if tot == 2:
    print(f'E por isso ele  é PRIMO.')
else:
    print('E por isso ele NÃO é PRIMO')
