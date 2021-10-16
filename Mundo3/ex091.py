"""
Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""

from random import randrange as rr
from time import sleep
from operator import itemgetter as it

jogadores = {'jogador_1': rr(1, 7),
             'jogador_2': rr(1, 7),
             'jogador_3': rr(1, 7),
             'jogador_4': rr(1, 7)}

ranking = list()
print('-*' * 15)
print('Valores sorteados: ')
print()
for k, v in jogadores.items():
    print(f'{k} tirou {v} no jogo.')
    sleep(1)
ranking = sorted(jogadores.items(), key=it(1), reverse=True)
print('-=' * 15)
print('RANKING dos jogadores: ')
print()
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
