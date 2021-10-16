'''Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.'''

C = str(input('Qual é a sua cidade?')).strip()
print (f'A sua cidade é {C}.')
print('O nome da sua cidade começa com Santo?')
print(C[:5].upper() == 'SANTO')

