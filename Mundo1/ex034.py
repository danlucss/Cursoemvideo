"""
Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
 Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
"""


print('Olá, gostaria de informar que você irá receber um aumento!')
print('-=-'*30)
print('Para salarios acima de R$1250.00, o aumento será de 10% e para salarios abaixo, o aumento será de 15%.')
print('-=-'*30)
salario = float(input('Quanto você recebe atualmente?'))
if salario >= 1250.00:
    salario = salario*0.10
    print(f'Você receberá um aumento de 10%, seu novo salario será de {(salario*0.10)+salario}')
else:
    salario = salario*0.15
    print(f'Você receberá um aumento de 15%, seu novo salario será de R${(salario*0.15)+salario}')
print('Muito obrigado pela sua colaboração em nossa empresa!')
