"""
Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.


"""

dicionario = {'nome': str(input('Nome: ')), 'media': float(input('Média: '))}

print('-=' * 20)
print(f'O aluno é {dicionario.get("nome")}')
print(f'Sua média é {dicionario.get("media")}.')
if dicionario.get('media') >= 6:
    print(f'O aluno foi aprovado!')
else:
    print(f'O aluno foi reprovado!')
