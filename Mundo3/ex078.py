"""
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
 No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.


"""

lista = [int(input('Insira um numero: ')),
         int(input('Insira um outro numero: ')),
         int(input('Insira mais um número: ')),
         int(input('Insira mais um numero: ')),
         int(input('Insira o ultimo numero: '))]
print(lista)
print(f'O maior valor da lista é {max(lista)} e está na posição {lista.index(max(lista))}')
print(f'O menor valor da lista é {min(lista)} e está na posição {lista.index(min(lista))}')
