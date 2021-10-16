"""
Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""


cont1 = 0
cont = 0
from datetime import date
atual = date.today().year
for c in range(1, 8):
    p = int(input(f'Em que ano a {c}ª pessoas nasceu? '))
    if atual - p >= 18:
        cont += 1
    else:
        cont1 += 1
print(f'{cont1} pessoas são menores de idade, {cont} pessoas já atingiram a maioridade.')
