"""
Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o
total de vitórias consecutivas que ele conquistou no final do jogo.
"""

from random import randint
from time import sleep
print('-=-'*20)
print('Vamos jogar PAR ou IMPAR?')
print('-=-'*20)
n = j = cont = 0
while True:
    pc = randint(0, 10)
    n = int(input('Diga um valor: '))
    j = ' '
    while j not in 'pi':
        j = str(input('É PAR ou IMPAR? [P/I]')).strip().lower()
    sleep(1)
    npc = n+pc
    if npc % 2 == 0:
        result = 'p'
        res = 'PAR'
    else:
        result = 'i'
        res = 'IMPAR'
    print('*'*30)
    print(f'Você jogou {n} e o computador jogou {pc}. O total é {n+pc} e o resultado é: {res}')
    print('*'*30)
    sleep(1)
    if j == result:
        cont += n
        print('-='*20)
        print('Parabéns você venceu!')
        print('Vamos jogar novamente?')
        print('-='*20)
    elif j != result:
        print('-='*20)
        print(f'Que pena, você perdeu!')
        print('-='*20)
        break
print(f'GAME OVER! Você ganhou {cont} vezes.')
