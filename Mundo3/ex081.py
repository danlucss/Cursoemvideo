"""
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na list
"""

lista = list()
cont = 0

while True:
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    resposta = str(input('Quer continuar? [S/N]: '))
    if resposta in "nN":
        break
print('_'*30)
print(f'Foram digitados {cont} números')
lista.sort()
print(f'A lista é {lista}.')
lista.sort(reverse=True)
print(f'A lista ao contrario é {lista} ')
if 5 in lista:
    print(f'O numero 5 está na lista e aparece na posição {lista.index(5)}.')
else:
    print('O numero 5 não está presente na lista.')
