"""
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
individualmente.
"""

ficha = list()

while True:
    Nome = str(input('Nome: '))
    Nota_1 = float(input('Nota 1: '))
    Nota_2 = float(input('Nota 2: '))
    media = Nota_1 + Nota_2 / 2
    ficha.append([Nome, Nota_1, Nota_2, media])
    resp = str(input('Deseja continuar? [S/N]'))
    if resp in 'Nn':
        break

print('-=' * 20)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-'*26)

for i, a in enumerate(ficha):
    print(f'{i+1:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-*')
    nota = int(input('Deseja ver as notas de qual aluno? [999] Para finalizar: '))
    if nota == 999:
        print('Finalizando...')
        break
    if nota <= len(ficha) - 1:
        print(f'Notas do aluno {ficha[nota][0]} são {ficha[nota][1]}.')
