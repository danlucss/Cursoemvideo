"""
Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""


from datetime import date
print('-=-'*20)
print('Calculadora de ano bissexto!')
ano = int(input('Digite um ano. Para o ano atual, digite 0: '))
print('-=-'*20)
if ano == 0:
    ano = date.today().year
print(f'O ano que você informou é {ano}, calculando...')

import time
time.sleep(2)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:

    print('O ano é bissexto!')
else:
    print('O ano não é bissexto!')
