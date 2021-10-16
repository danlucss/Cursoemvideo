"""
Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

numex = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
         'treze', 'quatorze', 'quinze', 'desesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num1 = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num1 <= 20:
        break
    print('Tente novamente.', end=' ')
print(f'Você digitou o número {numex[num1]}.')
