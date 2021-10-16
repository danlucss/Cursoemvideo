"""
Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.
"""

print('Tabuada 2.0')

n = int(input('Por favor, escolha um número:'))

for c in range(1, 11):
    print(f'{n} x {c:2} = {n * c}')
