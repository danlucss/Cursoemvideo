"""
Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""

print('Quer adquirir sua nova moradia? Nós te ajudamos!')
print('-==-' * 20)
print('Responda o questionario, e saberemos se o financiamento estára aprovado para você.')
print('-==-' * 20)
c = float(input('Qual o valor da casa que você deseja? R$'))
s = float(input('Quanto você recebe por mês? R$'))
t = int(input('Em quantos anos deseja pagar o financiamento da sua casa?'))
minimo = (s * 0.30)
prestacao = c / (t * 12)

print(f'''
    \033[35m O valor da casa de sua preferencia é de {c}, o seu salario é R${s:.2f}
     e você deseja pagar a casa em {t} anos.''')
print(f' O valor maximo das parcelas será: R${prestacao:.2f}.')
print(f'O valor maximo que você poderá pagar é de: R${minimo:.2f}.')
print('Calculando...')
from time import sleep

sleep(3)
if minimo >= prestacao:
    print('\033[36m O financiamento será aprovado!')
else:
    print('\033[36m O financiamento não será aprovado!')
