'''
Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e
do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.'''

import math
a= float(input('Digite o valor do cateto adjacente:'))
b= float(input('Digite o valor do cateto oposto:'))
c = math.hypot(a,b)
print (f'Se o comprimento do cateto oposto é {b} e do cateto adjacente é {a}, então a sua hipotenusa é {c:.3f}')