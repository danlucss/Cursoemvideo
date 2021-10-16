"""
Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""

print('Calculadora de PA 2.0')
print('=-='*8)
primeiro = int(input('Qual o primeiro termo da PA?'))
razao = int(input('Qual a razão da PA?'))
termo = primeiro
c = 1
from time import sleep

print('Calculando...')
sleep(1)

while c <= 10:
    print(f'{termo} →', end='')
    termo += razao
    c += 1
print('FIM')
