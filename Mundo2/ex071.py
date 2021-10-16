"""
Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

print('=-'*15)
print('{:^30}'.format('Shadow BANK'))
print('=-'*15)

n = int(input('Quanto você deseja sacar: '))
total = n
ced = 50
cedtotal = 0
while True:
    if total >= ced:
        total -= ced
        cedtotal += 1
    else:
        if cedtotal > 0:
            print(f'O total de {cedtotal} cédulas de R${ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        cedtotal = 0
        if total == 0:
            break
print('='*30)
print('Muito obrigado, e volte sempre a SHADOW BANK.')
