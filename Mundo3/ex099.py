"""
Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores
inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""


def maior(* valores):
    a = max(valores)
    print(f'O maior valor entre {valores} é {a}.')


maior(1, 10, 29, 3, 5)
maior(12231, 1, 312113, 63423423, 656747456, 2)
