"""
Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais
"""

n1 = int(input('Digite um valor:'))
n2 = int(input('Digite um segundo valor:'))
print(f'Você escolheu: \033[32m {n1} \033[m e \033[34m {n2} \033[m.')
if n1 > n2:
    print(f'\033[32m O primeiro valor é o maior.\033[m')
elif n2 > n1:
    print(f'\033[34m O segundo valor é o maior.\033[m')
elif n1 == n2:
    print('Não existe valor maior. Os dois valores são iguais.')
