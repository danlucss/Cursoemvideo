'''
Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
'''


import math
n= float(input ('Digite um número:'))
print (f'A parte real desse numero é {n}, e sua porção inteira é {math.floor(n)}')