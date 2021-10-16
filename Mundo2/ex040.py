"""
Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO
"""

print('Calculadora de médias')
print('-' * 40)
n1 = float(input('Qual a sua nota de n1? '))
n2 = float(input('Qual a sua nota de n2? '))
m = (n1 + n2) / 2
print(f'Sua nota de n1 foi {n1} e sua nota de n2 foi {n2}. Sua media é {m}.')

if m < 5.0:
    print('Você foi reprovado! Precisa se esforçar mais.')
elif m > 7.0:
    print('Parabéns! Você foi aprovado!')
else:
    print('Precisa melhorar mais... Está em Recuperação...')
