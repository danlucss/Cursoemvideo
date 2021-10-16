"""
Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
"""

from random import randint

print('-*' * 20)
print('Jogo da advinhação 2.0 - Python!')
print('-*' * 20)
computer = randint(0, 10)
player = int(input('Digite um número, entre 0 e 10: '))
cont = 0
while computer != player:
    player = int(input('Por favor, tente novamente:'))
    cont += 1
print(
    f'Parabens você acertou! O número que você digitou foi {player}, e o que eu escolhi foi {computer}. Porém, você '
    f'precisou de {cont} tentativas.')
