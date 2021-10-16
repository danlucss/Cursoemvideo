'''
Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.'''

nome= str(input('Qual o seu nome completo?'))
nc= nome.count(nome)
nl= len(nome.replace(' ',''))
nd= nome.split()
ni= len(nd[0])
print (nome)
print(nome.lower())
print (nome.upper())
print(f'O seu nome tem {nl} letras, e seu primeiro nome tem {ni} letras.')