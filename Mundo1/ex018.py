'''Exercício Python 18: Faça um programa que leia um ângulo qualquer
 e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''

import math
a= int(input('Digite o angulo que deseja:'))
s= math.sin(math.radians(a))
c= math.cos(math.radians(a))
t= math.tan(math.radians(a))

print (f'Se o angulo é {a}, o seno é {s:.2f}, o cosseno é {c:.2f} e a tangente é {t:.2f}.')