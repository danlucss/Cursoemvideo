"""
Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120
"""


print('Calculadora de fatorial 2.0')
print('=='*10)
n = int(input('Informe o número para calcular o seu fatorial: '))
m = 1
for f in range(n, 0, -1):
    print(f'{f}', end='')
    print('x' if f > 1 else '=', end='')
    m *= f
    f -= 1
print(f' {m}\n O fatorial de {n}! é {m}.')
