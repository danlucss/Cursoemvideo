"""
Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER
"""

from datetime import date

print('''
    \033[1;34m Confederação Brasileira de Natação\033[m\nPrecisamos saber em qual categoria nossos atletas se encaixam.
    ''')
print('Por favor, preencham o formulario.')
n = str(input('Informe seu nome: '))
ano = int(input('Informe o ano do seu nascimento: '))
atual = date.today().year
idade = atual - ano
print(f'Você é {n}, nascido em {ano} e tem {idade} anos de idade.')

if idade <= 9:
    print('Muito bem, você é da categoria MIRIM.')
elif idade <= 14:
    print('Excelente! Você é da categoria INFANTIL')
elif idade <= 19:
    print('Uau! Você é da categoria JUNIOR.')
elif idade <= 25:
    print('Incrivel! Você é da categoria SENIOR')
elif idade > 25:
    print('Otimo! Você é da categoria MASTER.')

print(' A Confederação Brasileira de Natação, agradece a sua colaboração. Tenha um bom dia!')
