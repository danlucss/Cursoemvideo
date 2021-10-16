"""Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista compost """

from random import randint

print('*-' * 15)
print(f'MEGA SENA SIMULATOR')
print('*-' * 15)

lista = list()
jogos = list()
tot = 1
quantidade = int(input('Quantos jogos você quer que eu faça? '))
while tot <= quantidade:
    cont = 0
    while True:
        num = randint(1, 61)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'-=' * 3, f'SORTEANDO {cont} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'JOGO {i + 1} : {l}.')
