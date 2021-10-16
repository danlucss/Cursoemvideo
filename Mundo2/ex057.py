"""
Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

sexo = ''
while sexo != ['M', 'F']:
    sexo = str(input('Infome seu sexo: [M/F]')).strip().upper()[0]

    if sexo in 'M':
        print('Sexo Masculino computado com sucesso.')
        break
    elif sexo in 'F':
        print('Sexo Feminino computado com sucesso.')
        break
    else:
        print('Por favor, digite um valor valido: [M/F]')
