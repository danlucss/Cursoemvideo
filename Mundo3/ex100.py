"""
Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar()
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
todos os valores pares sorteados pela função anterior.
"""

from random import randint as ri
from time import sleep


def sorteia(lista):
    print('Sorteando os 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = ri(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=False)
        sleep(0.3)
    print('>>PRONTO<<')


def soma_par(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {lista}, temos {soma}.')


numeros = list()
sorteia(numeros)
soma_par(numeros)
