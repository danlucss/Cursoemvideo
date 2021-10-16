"""
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
em um dicionário e todos os dicionários em uma lista.
No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de
pessoas com idade acima da média.
"""

pessoas = dict()
galera = list()
soma = media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoas['sexo'] in "MF":
            break
        print('Error. Dados invalidos. Apenas M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    galera.append(pessoas.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in "SN":
            break
        print('Error. Dados invalidos. Apenas S ou N.')
    if resp in 'N':
        break
print('-*' * 30)
media = soma / len(galera)
print(galera)
print(f'Ao todo foram cadastradas {len(galera)} pessoas.')
print(f'A media de todas as idades é {media:5.2f} anos.')
print('As mulheres cadastradas foram:', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('Lista de pessoas que estão acima da média de idade: ')
for p in galera:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f' {k}  =  {v} ', end='')
        print()
print('>>>>ENCERRADO<<<<')
