"""
Exercício Python 29: Escreva um programa que leia a velocidade de um carro.
 Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
 A multa vai custar R$7,00 por cada Km acima do limite.
"""


from random import randint

km = randint(40, 200)
print(f' O seu carro está correndo a: {km} kms por hora!')
if km > 80:
    print(f'Você foi multado! \n A sua multa vai ser de:{(km-80)*7} R$')
else:
    print('Parabéns! Você está dentro da velocidade permitida!')
print('Faça uma boa viagem!')
