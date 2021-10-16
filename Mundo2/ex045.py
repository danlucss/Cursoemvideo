"""
Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
"""

from random import randint

jogadas = ('PEDRA', 'PAPEL', 'TESOURA')
print('Jo... ken... PC!')
print('-=-' * 30)
print('Se você acha que pode vencer o computador.... Siga em frente.')
from time import sleep

sleep(2)
print('''Suas opções são:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
voce = int(input('\033[1;32mFaça sua jogada: \033[m'))
PC = randint(0, 2)
sleep(1)
print('Jo...')
sleep(1)
print('Ken...')
sleep(1)
print('PC!')
sleep(2)
print('-=' * 11)
print(f'Sua jogada foi {(jogadas[voce])}')
print(f'A jogada do PC foi {(jogadas[PC])}')
print('-=' * 11)

if PC == 0:  # computador usa pedra
    if voce == 0:
        print('EMPATE')
    elif voce == 1:
        print('JOGADOR VENCE!')
    elif voce == 2:
        print('PC VENCE!')

if PC == 1:  # PC usou papel
    if voce == 0:
        print('PC VENCE!')
    elif voce == 1:
        print('EMPATE!')
    elif voce == 2:
        print('JOGADOR VENCE!')

if PC == 2:  # PC usou TESOURA
    if voce == 0:
        print('JOGADOR VENCE')
    elif voce == 1:
        print('PC VENCE!')
    elif voce == 2:
        print('EMPATE')
