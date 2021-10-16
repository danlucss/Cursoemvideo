"""
Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
"""

print('\033[1;35mIniciando a conversora Python 1.0... \033[m')
from time import sleep

sleep(2)
n = int(input('Digite um número inteiro:'))

print('''Para qual base de arquivo deseja a conversão:
Para binario digite [1]
Para octal digite [2]
Para hexadecimal digite [3]''')

c = int(input('Escolha a base de arquivo:'))
print(f'O número escolhido foi: {n}.')
if c == 1:
    print(f'Em binario ele será: {bin(n)}. ')
elif c == 2:
    print(f'Em octal ele será: {oct(n)}.')
elif c == 3:
    print(f'Em hexadecimal ele será: {hex(n)}.')
else:
    print('Error. Base de arquivo não reconhecida. Finalizando...')
sleep(2)
print('Até logo!')
