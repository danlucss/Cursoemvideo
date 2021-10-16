"""
Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

a = int(input('Por favor, digite um numero:'))
b = int(input('Por favor, digite um outro número:'))
c = int(input('Por favor, digite mais um número:'))

print(f'Os números que você digitou foram: {a, b, c}')
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(f'O menor é {menor}.')
maior = b
if a > b and a > c:
    maior = a
if c > b and c > a:
    maior = c
print(f'O maior é {maior}.')
