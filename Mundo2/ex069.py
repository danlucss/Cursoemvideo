"""
Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
"""


c1 = c2 = c3 = 0
while True:
    nome = str(input('Informe o seu nome: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()
    idade = int(input('Informe sua idade: '))
    print('Cadastramento concluido.')
    if idade >= 18:
        c1 += 1
    if sexo in 'M':
        c2 += 1
    if sexo in 'F' and idade <= 20:
        c3 += 1
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar com o cadastramento? [S/N] ')).strip().upper()
    if escolha in 'N':
        print('Encerrando programa...Aguarde.')
        break
print(f'Ao todo são {c1} pessoas maiores de 18 anos. ')
print(f'Ao todo {c2} homens foram cadastrados.')
print(f'Ao todo {c3} mulheres com menos de 20 anos, foram cadastradas.')
print('Programa finalizado.')
