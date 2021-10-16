"""
Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
retangular (largura e comprimento) e mostre a área do terreno.
"""


def area():
    print('Controle de Terrenos')
    print('-'*20)
    b = float(input('LARGURA (m): '))
    h = float(input('COMPRIMENTO (m): '))
    a = b * h
    print(f'A área de um terreno {b}x{h} é de {a:.1f}m².')


area()
