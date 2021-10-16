'''Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa,
 mostrando em seguida o primeiro e o último nome separadamente.'''

n = str(input('Informe seu nome completo: ')).strip()
nome = n.split()
primeiro_nome = nome[0]
ultimo_nome = nome[-1]
print(f'Seu nome é {n}.')
print(f'Seu primeiro nome é {primeiro_nome}.')
print(f'Seu ultimo nome é {ultimo_nome}.')