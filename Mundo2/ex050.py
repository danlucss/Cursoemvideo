"""
Exercício Python 50: Desenvolva um programa que leia seis números inteiros e
mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""


print('-*' * 18)
print('OS 10 PRIMEIROS TERMOS DE UMA P.A.')
print('-*' * 18)

primeiro = int(input('Qual o primeiro elemento: '))
razao = int(input('Qual é a razão: '))
n = 10
ultimo = primeiro + (n-1) * razao
ultimo = ultimo + 1
# n = int(input('Quantos elementos exibir: '))
print(f'Primeiro termo: {primeiro}.')
print(f'A razão é: {razao}')


pa: int
for pa in range(primeiro, ultimo, razao):
    print(f'{pa} ', end='→')
print('ACABOU')
