'''Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.'''

n= str(input('Qual o seu nome completo?')).strip()
n1= ('SILVA' in n.upper().split())
print(f'O seu nome é {n}. \nO seu nome tem Silva?')
if n1<=0:
    print ('Não!')
else:
    print('Sim!')

