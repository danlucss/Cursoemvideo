"""
Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de
mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes
"""

print('Vamos saber se três retas formam um triângulo?')
print('-' * 40)
a = float(input('Qual o comprimento da primeira reta?'))
b = float(input('Qual o comprimento da segunda reta?'))
c = float(input('Qual o comprimento da terceira reta?'))

print(f'O comprimento das retas que você colocou são, respectivamente: {a}cm, {b}cm, {c}cm. ')
if (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b:
    print('As retas formam um triangulo.')
    if a == b == c:
        print('O triangulo é um equilatero')
    elif a != b != c != a:
        print('O triangulo é escaleno.')
    else:
        print('O triangulo é isosceles.')
else:
    print('As retas não formam um triangulo.')
    exit()
