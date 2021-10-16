"""
Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
"""


print('Vamos saber se três retas, formam um triangulo?')
print('-_-'*20)
a = float(input('Qual o comprimento da primeira reta?'))
b = float(input('Qual o comprimento da segunda reta?'))
c = float(input('Qual o comprimento da terceira reta?'))
print(f'O comprimento das retas que você digitou foram: {a}cm, {b}cm, {c}cm.')
if (b-c) < a < b + c and (a-c) < b < a + c and (a-b) < c < a + b:
    print('As retas formam um triangulo.')
else:
    print('As retas não formam um triangulo.')
