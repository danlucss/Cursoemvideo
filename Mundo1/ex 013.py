"""
Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário
e mostre seu novo salário, com 15% de aumento.
"""


s = float(input('Quanto você recebe?'))
ns = s*15/100+s
print(f'O seu salario de {s}R$, receberá um aumento de 15%, indo para {ns}R$.')
