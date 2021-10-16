"""
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""

lista = list()
dados = list()

maior_peso = 0
menor_peso = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))

    resposta = str(input('Quer continuar? [S/N]: '))
    if resposta in 'Nn':
        break
    if len(dados) == 0:
        maior_peso = menor_peso = dados[1]
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        if dados[1] < menor_peso:
            menor_peso = dados[1]
    lista.append(dados[:])
    dados.clear()
print('-=' * 30)
print(f'Ao todo foram cadastrados {len(lista)} pessoas.')
print(f'O menor peso é {menor_peso}.')
for p in lista:
    if p[1] == menor_peso:
        print(f'{p[0]}', end='')
print(f'O maior peso é {maior_peso}KG', end='')
for p in lista:
    if p[1] == maior_peso:
        print(f'{p[0]}', end=' ')
