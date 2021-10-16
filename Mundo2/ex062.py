"""
Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
"""


print('Calculadora de PA 2.0')
print('=-='*8)
primeiro = int(input('Qual o primeiro termo da PA?'))
razao = int(input('Qual a razão da PA?'))
termo = primeiro
c = 1
total = 0
mais = 10
from time import sleep

print('Calculando...')
sleep(1)

while mais != 0:
    total = total + mais
    while c <= total:
        print(f'{termo} →', end='')
        termo += razao
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print('FIM')
