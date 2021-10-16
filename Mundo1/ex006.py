'''Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.'''

from math import sqrt
n = int(input('Digite um número inteiro: '))

print(f'O número informado é {n}.\nSeu dobro é {n*2}.\nSeu triplo é {n*3}.\nE a raiz quadrada deste número é {sqrt(n):.2f} ')