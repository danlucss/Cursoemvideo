"""
Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""


print('Olá, quer uma forma fácil de saber se um número é par ou impar? É só me perguntar!')
n = int(input('Qual número deseja saber?'))

if n % 2 == 0:
    print(f'O número {n} é par!')
else:
    print(f'O número {n} é impar!')

print('Muito obrigado!')
