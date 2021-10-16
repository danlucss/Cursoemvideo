"""
Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""


from random import randint
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5, e quero ver você adivinhar!')
print('-=-'*20)

numero = randint(0, 5)
duvida = int(input(' Então, qual é o número?'))
if numero != duvida:
    print(f'Poxa era {numero}, não foi dessa vez!')
else:
    print(f'Uau! O numero é {numero}! Você é fera! Acertou na mosca!')
